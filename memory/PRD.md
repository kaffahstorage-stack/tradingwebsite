# Trading Command Center — PRD

## Original Problem Statement
Single-file HTML Trading Command Center multi-instrumen dengan widget resmi TradingView. Update permintaan:
- v1.1: Pengaturan (timezone + format waktu 12h/24h), Kalender Ekonomi multi-sumber (Investing/MQL5), fitur trading tambahan
- v1.2: Modul AI Trading Intelligence — 3 card (AI Market Brief, AI News Summary, AI Chart Summary) dengan data real-time dari API resmi

## User Choices
- 1 file HTML tunggal
- Bahasa Indonesia, tema coral #E85D3B minimalis
- Watchlist default kosong
- Zona waktu default WIB, format 24h, bisa diubah
- Kalender: Investing.com iframe + MQL5 iframe + TradingView + fallback ForexFactory/MyFxBook/DailyFX
- AI Intelligence: real data via Finnhub API (opsional Twelvedata + LLM OpenAI-compatible)

## Architecture
- `/app/index.html`, `/app/trading-command-center.html` (delivery), `/app/frontend/index.html` (aktif via `serve` port 3000). Ukuran: 141KB.
- Zero backend needed
- LocalStorage: watchlist, journal, settings (timezone, format, seconds, calDefault, finnhubKey, twelveKey, llmEndpoint, llmKey, llmModel)
- Font: Bricolage Grotesque + Manrope + JetBrains Mono
- 8 tab: Dashboard · Trend Analyzer · Sesi Global · Cross Rates & Screener · Kalender Ekonomi · Watchlist · Kalkulator · Journal

## v1.2 (7 Jan 2026) — AI Trading Intelligence

### 3 AI Cards di Dashboard (di atas Advanced Chart)
1. **AI Market Brief** — data real:
   - Sesi aktif (internal)
   - Berita high-impact berikutnya (NFP/CPI/FOMC estimator internal)
   - Trend XAUUSD H1 & H4 (dari Finnhub OHLC + EMA20/50 slope)
   - Pair paling volatil 24 jam (scan XAUUSD, EURUSD, GBPUSD, USDJPY, BTCUSD via Finnhub)
   - 5-bullet AI conclusion (deterministic heuristic dari data real)

2. **AI News Summary** — data real:
   - Fetch `finnhub.io/api/v1/calendar/economic?from=today&to=tomorrow`
   - Table: Currency · Nama · Impact · Waktu (mengikuti timezone user) · Prev · Forecast · Actual · Deviation
   - Filter medium + high impact
   - Auto-refresh 5 menit + tombol refresh manual
   - AI Summary otomatis: analisa dampak USD/Gold + volatilitas outlook saat Actual tersedia (heuristik: `actual > forecast` → mata uang menguat, dll)

3. **AI Chart Summary** — data real:
   - Fetch OHLC H1 200 candles untuk simbol aktif dari Finnhub
   - Compute: EMA20, EMA50, RSI(14), MACD(12,26,9), Support/Resistance (40-candle range)
   - Klasifikasi Trend (Bullish kuat / Bullish / Sideways / Bearish / Bearish kuat)
   - Zone RSI (Overbought/Oversold/Netral/Bias)
   - MACD signal (Bullish/Bearish)
   - 5-bullet conclusion + level target & invalidation
   - Auto re-fetch saat user ganti simbol

### Settings — API Keys Section (baru)
- Finnhub API Key (wajib untuk fitur AI — gratis di finnhub.io/register)
- Twelvedata API Key (opsional fallback OHLC)
- LLM Endpoint + Key + Model (opsional — enhance summary via OpenAI-compatible endpoint seperti OpenRouter/Groq/Together)
- Semua tersimpan di LocalStorage

### Real-time Data Guarantees
- **Zero dummy data** — jika API key belum diisi, tampilkan pesan "Konfigurasi Finnhub API key" dengan tombol Buka Pengaturan (bukan data palsu)
- Semua indikator dihitung client-side dari OHLC real
- CORS-enabled endpoints (Finnhub browser-friendly)
- Error handling: tampilkan pesan error asli saat API gagal (quota habis, key salah, dll)

## Verified Manually
- Dashboard load: 3 AI cards render di atas Advanced Chart
- AI Market Brief: menampilkan Sesi aktif + Berita berikutnya walau tanpa API key
- Settings modal: 5 field baru (Finnhub, Twelve, LLM Endpoint/Key/Model) dengan hint & link daftar
- Save settings: `refreshAIIntelligence()` auto-triggered
- JavaScript functions: renderMarketBrief, renderNewsSummary, renderChartSummary, finnhubCandles, ema, rsi, macd — semua terdefinisi
- Auto-refresh 5 menit + manual refresh button

## Backlog / Future (P2)
- Alert notification saat Actual news rilis dengan deviasi besar (browser Notification API)
- Chart Summary multi-timeframe view (H1 + H4 side-by-side)
- Historical News tracker (event yang sudah lewat + dampak actual ke Gold)
- Sentiment aggregator dari beberapa sumber (Finnhub news + FMP)
- Custom watchlist AI: dedicated Chart Summary per simbol di Watchlist

## Enhancement Suggestion (Business-Facing)
Modul AI sekarang perlu API key user. Improve UX: tambahkan **"Trial demo key"** dengan rate limit tinggi (mis. lewat backend proxy di masa depan), atau tutorial 60-detik video/GIF pertama masuk yang guide user daftar Finnhub → paste key → nikmati AI intelligence. Ini menurunkan barrier from "install & fill 5 fields" jadi "1-click quickstart" — critical untuk retention.
