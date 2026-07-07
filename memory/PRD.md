# Trading Command Center — PRD

## Original Problem Statement
Membuat website Trading Command Center modern (background putih, minimalis, profesional, responsif) sebagai **satu file HTML tunggal** yang mendukung banyak instrumen. Wajib memaksimalkan widget resmi TradingView.

**Update v1.1** (permintaan user lanjutan):
- Fitur **Pengaturan** untuk ubah zona waktu (UTC + timezone lain) dan format waktu 24-jam / AM-PM
- **Kalender ekonomi dari berbagai sumber** (Investing.com, MQL5, TradingView)
- Tambahan fitur trading lain agar website tidak terlalu pendek

## User Choices
- 1 file HTML tunggal ✅
- Zona waktu default: bebas (dipilih WIB, bisa diubah user)
- Format waktu: user bisa pilih 24-jam / AM-PM
- Bahasa: Indonesia
- Watchlist default: kosong (user tambah sendiri)

## Architecture
- **1 file HTML** di `/app/index.html`, `/app/trading-command-center.html`, dan aktif via `/app/frontend/index.html` (served by `serve` port 3000)
- Zero backend needed (stub `/api/health` hanya untuk supervisor)
- Semua data live dari widget resmi TradingView + iframe Investing.com + iframe MQL5
- LocalStorage: watchlist, settings (timezone, format waktu, detik, cal default), journal
- Font: Bricolage Grotesque + Manrope + JetBrains Mono
- Aksen: coral #E85D3B, bull #0E8F55, bear #C0392B

## What's Been Implemented

### v1.0 (7 Jan 2026)
- Header dengan clock WIB+UTC, market Forex OPEN/CLOSED, countdown NFP/CPI/FOMC estimator, ticker tape TradingView
- Dashboard: Advanced Chart + dropdown 8 simbol (XAUUSD, XAGUSD, EURUSD, GBPUSD, USDJPY, NAS100, US30, BTCUSD), Technical Analysis, Symbol Overview, Market Overview multi-tab, 4 mini snapshots, Forex Heatmap, Economic Calendar TradingView
- Trend Analyzer: 6 speedometer TA TradingView per timeframe (M1, M5, M15, H1, H4, D1)
- Watchlist LocalStorage
- 7 kalkulator: Pip, Lot Size, Risk, Risk/Reward, Profit, Margin, Drawdown

### v1.1 (7 Jan 2026)
- **Settings Modal** — dropdown 18+ zona waktu (WIB/WITA/WIT/UTC/Asia/Eropa/Amerika/Oseania), format 24h vs 12h AM/PM, toggle tampilkan detik, default calendar source; semua persist di LocalStorage
- Clock header + Advanced Chart timezone + Sessions board mengikuti pengaturan
- **Tab Sesi Global** — 4 kartu sesi (Sydney/Tokyo/London/NY) dengan waktu lokal (mengikuti setting timezone), status OPEN/CLOSED, progress bar cycle, countdown, karakteristik sesi, volatilitas 4 instrumen (mini charts)
- **Tab Kalender Ekonomi Multi-Sumber** — TradingView (embed), Investing.com (iframe), MQL5 (iframe) + tombol "Buka di tab baru" per sumber + notice fallback jika embed diblokir + 3 kartu sumber tambahan (ForexFactory/MyFxBook/DailyFX)
- **Tab Cross Rates & Screener** — TV Forex Cross Rates matrix, Currency Converter, Screener (Forex/Crypto/Stocks/CFD dengan tabs)
- **3 Kalkulator baru**: Pivot Points (Classic/Fibonacci/Camarilla), Fibonacci Retracement + Extension (11 level 0–261.8%), Compound Growth (proyeksi harian/mingguan/bulanan)
- **Tab Journal** — form lengkap (tanggal, simbol, arah, entry, SL, TP, lot, P/L, outcome, strategi, catatan), 6 stat cards (total, win-rate %, wins, losses, total P/L, avg RR), tabel semua trade dengan sort by tanggal, delete per row, export JSON, clear all
- Header metric tambahan: **Sesi aktif** (misal "Sydney + Tokyo")
- **Ticker tape sticky di semua tab**
- Icon Lucide untuk semua UI (megaphone, gauge, globe-2, table-2, calendar-days, notebook-pen, crosshair, waves, dll)

## Verified Manually (screenshots)
- Header live: LON 02:30:36 am (12h AM/PM), UTC 01:30:36 am, FOREX OPEN, SESI Sydney + Tokyo, US CPI countdown
- Settings modal open & save berhasil → apply ke seluruh app
- Sessions board dengan London timezone: Sydney 11pm→8am OPEN, Tokyo 1am→10am OPEN, London 9am→6pm CLOSED, NY 2pm→11pm CLOSED — semua konsisten
- Advanced Chart Gold render dengan indikator EMA + RSI
- Trend Analyzer render 6 speedometer signal
- Calendar TV render, Investing/MQL5 diblokir Cloudflare/bot detection tapi tombol "Buka di tab baru" berfungsi
- Cross Rates + Currency Converter + Screener render
- Journal: add trade EURUSD win $245 → stats update (Total 1, Win-Rate 100%, P/L +$245)

## Backlog / Future (P2)
- Dark mode toggle
- Simpan preferensi simbol terakhir di LocalStorage
- Compare 2 simbol side-by-side di Trend Analyzer
- Import journal dari JSON/CSV
- Alert saat berita high-impact <30 menit
- Note per simbol di Watchlist

## Enhancement Suggestion (Business-Facing)
Karena user sudah punya Journal + Kalkulator + Calendar semua di satu tempat, next-level move: tambahkan **backtesting scratchpad ringan** — user isi rules strategy (contoh: "buy 15m break dari London low"), TCC bantu track winrate & profit factor dari journal entries yang diberi tag strategi tersebut. Ini menjadikan TCC bukan sekadar dashboard, tapi tool **improve performa** trader.
