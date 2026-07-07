# Trading Command Center — PRD

## Original Problem Statement
Membuat website Trading Command Center modern (background putih, minimalis, profesional, responsif) sebagai **satu file HTML tunggal** (HTML + CSS + JavaScript) yang mendukung banyak instrumen (Gold, Silver, Forex, Indeks, Crypto). Wajib memaksimalkan penggunaan widget resmi TradingView untuk chart & data.

## User Choices (verbatim)
- File output: **satu file HTML tunggal (`index.html`)**
- Economic Calendar & High Impact News: **widget Economic Calendar TradingView + countdown estimasi mock**
- Bahasa UI: **Indonesia**
- Tema warna aksen: **terserah agen** → dipilih *warm coral (#E85D3B)* di atas latar putih, dengan bull green + bear red trading klasik
- Watchlist: **kosong (user tambah sendiri)**

## Architecture
- **1 file HTML** di `/app/index.html` dan `/app/trading-command-center.html` (delivery copy). File aktif dijalankan dari `/app/frontend/index.html` via `serve` di port 3000.
- Zero backend needed (backend hanya stub `/api/health` agar supervisor sehat).
- Semua data live berasal dari widget resmi TradingView (chart, market overview, heatmap, technical analysis, economic calendar, symbol info, mini symbol, single quote, ticker tape).
- LocalStorage untuk persistensi watchlist (`tcc.watchlist.v1`).
- Font: Bricolage Grotesque (display) + Manrope (UI) + JetBrains Mono (angka).

## What's Been Implemented (7 Jan 2026)
- **Header**: brand, jam real-time WIB & UTC, status market Forex (OPEN/CLOSED via UTC schedule), countdown next high-impact event (NFP/CPI/FOMC estimator dinamis).
- **Ticker Tape TradingView** (Gold, Silver, EURUSD, GBPUSD, USDJPY, NAS100, US30, BTCUSD).
- **Dashboard**: Advanced Chart TradingView + dropdown 8 simbol (XAUUSD, XAGUSD, EURUSD, GBPUSD, USDJPY, NAS100, US30, BTCUSD), Technical Analysis speedometer 1H (sync dengan simbol dipilih), Symbol Overview, Market Overview multi-tab (Indices/Forex/Commodities/Crypto), 4 Mini Symbol snapshots, Forex Heatmap, Economic Calendar high+medium importance.
- **Trend Analyzer**: 6 kartu Technical Analysis TradingView per timeframe (M1, M5, M15, H1, H4, D1) dengan sinyal aktual + dropdown ganti simbol.
- **Watchlist**: input simbol (auto-normalize exchange prefix), tombol Tambah/Bersihkan, kartu per-simbol dengan Single Quote + Mini Symbol Overview, LocalStorage persistence, tombol hapus per item.
- **Kalkulator (7 kalkulator, live-recalc)**: Pip, Lot Size (position sizing), Risk, Risk/Reward, Profit, Margin, Drawdown (dengan recovery %).
- **Responsive**: breakpoint 1100px (kolom collapse) & 720px (mobile). Ticker tape overflow.
- **data-testid** pada semua elemen interaktif.

## Verified Manually (via screenshot)
- Dashboard render TradingView Advanced Chart Gold + speedometer XAUUSD 1H → **Neutral**.
- Trend Analyzer render 6 speedometer XAUUSD (M1 Sell, M5 Strong Sell, M15 Sell, H1 Sell, H4 Neutral, D1 Sell).
- Watchlist tambah EURUSD → widget Single Quote + Mini Chart tampil.
- Kalkulator: input default → Lot Size 0.200 lot, Risk $100, RR 1:3 (semua matematika benar).
- Countdown: `US CPI Release 6h 11:51:29` berjalan.
- Market: `FOREX OPEN`.

## Backlog / Future
- P2: Simpan preferensi simbol terakhir (bukan hanya watchlist) di LocalStorage.
- P2: Toggle dark mode manual (saat ini semua widget di-force light theme).
- P2: Multi-simbol Technical Analysis di tab Trend Analyzer (compare 2 simbol side-by-side).
- P2: Import/export watchlist ke JSON/CSV.
- P2: Countdown expand ke seluruh event mingguan (bukan hanya CPI/NFP/FOMC).

## Enhancement Suggestion (Business-Facing)
Karena ini command center **pribadi**, potensi peningkatan yang paling relevan: tambahkan **"Trade Journal"** ringan yang tersimpan di LocalStorage (entry, SL, TP, alasan, hasil actual) — sehingga trader bisa cross-reference sinyal Trend Analyzer dengan performa riilnya. Ini bisa jadi jembatan menuju versi web-app berbayar.
