# BANSHAP Website — Delete Unused Files
# Run this script in PowerShell to remove all unused assets
# Safe to run: all files listed here are NOT referenced in any HTML or CSS file

$root = "C:\Users\PC\Documents\BANSHAP INVESTMENT COMPANY LIMITED"

Write-Host "Cleaning up unused files..." -ForegroundColor Cyan

# ── Bootstrap CSS extras (only bootstrap.min.css is used) ─────────────────────
Remove-Item "$root\assets\vendor\bootstrap\css\bootstrap-grid*" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\bootstrap\css\bootstrap-reboot*" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\bootstrap\css\bootstrap-utilities*" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\bootstrap\css\bootstrap.css" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\bootstrap\css\bootstrap.css.map" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\bootstrap\css\bootstrap.min.css.map" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\bootstrap\css\bootstrap.rtl*" -Force -ErrorAction SilentlyContinue
Write-Host "  [OK] Bootstrap CSS extras removed" -ForegroundColor Green

# ── Bootstrap JS extras (only bootstrap.bundle.min.js is used) ────────────────
Remove-Item "$root\assets\vendor\bootstrap\js\bootstrap.js" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\bootstrap\js\bootstrap.js.map" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\bootstrap\js\bootstrap.min.js" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\bootstrap\js\bootstrap.min.js.map" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\bootstrap\js\bootstrap.bundle.js" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\bootstrap\js\bootstrap.bundle.js.map" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\bootstrap\js\bootstrap.bundle.min.js.map" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\bootstrap\js\bootstrap.esm*" -Force -ErrorAction SilentlyContinue
Write-Host "  [OK] Bootstrap JS extras removed" -ForegroundColor Green

# ── Bootstrap Icons extras (only bootstrap-icons.css is used) ─────────────────
Remove-Item "$root\assets\vendor\bootstrap-icons\bootstrap-icons.json" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\bootstrap-icons\bootstrap-icons.min.css" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\bootstrap-icons\bootstrap-icons.scss" -Force -ErrorAction SilentlyContinue
Write-Host "  [OK] Bootstrap Icons extras removed" -ForegroundColor Green

# ── AOS extras (only aos.css and aos.js are used) ─────────────────────────────
Remove-Item "$root\assets\vendor\aos\aos.cjs.js" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\aos\aos.esm.js" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\aos\aos.js.map" -Force -ErrorAction SilentlyContinue
Write-Host "  [OK] AOS extras removed" -ForegroundColor Green

# ── Glightbox extras (only glightbox.min.css and glightbox.min.js are used) ───
Remove-Item "$root\assets\vendor\glightbox\css\glightbox.css" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\vendor\glightbox\js\glightbox.js" -Force -ErrorAction SilentlyContinue
Write-Host "  [OK] Glightbox unminified files removed" -ForegroundColor Green

# ── Swiper extras (source map not needed) ────────────────────────────────────
Remove-Item "$root\assets\vendor\swiper\swiper-bundle.min.js.map" -Force -ErrorAction SilentlyContinue
Write-Host "  [OK] Swiper source map removed" -ForegroundColor Green

# ── Unused images ─────────────────────────────────────────────────────────────
Remove-Item "$root\assets\img\hero-img.png" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\why-us.png" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\bg" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\cta" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\illustration" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\person" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\services" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\steps" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\clients" -Recurse -Force -ErrorAction SilentlyContinue
Write-Host "  [OK] Unused image folders removed" -ForegroundColor Green

# ── Unused blog images (square images 1-5 are kept; hero and post 1-4 are not)
Remove-Item "$root\assets\img\blog\blog-hero-2.webp" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\blog\blog-post-1.webp" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\blog\blog-post-2.webp" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\blog\blog-post-3.webp" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\blog\blog-post-4.webp" -Force -ErrorAction SilentlyContinue
Write-Host "  [OK] Unused blog images removed" -ForegroundColor Green

# ── Unused portfolio images (logistics-1, digital-portal, cargo-trucks are kept)
Remove-Item "$root\assets\img\portfolio\portfolio-1.webp" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\portfolio\portfolio-3.webp" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\portfolio\portfolio-4.webp" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\portfolio\portfolio-7.webp" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\portfolio\portfolio-8.webp" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\portfolio\portfolio-9.webp" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\portfolio\portfolio-10.webp" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\portfolio\portfolio-portrait-1.webp" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\portfolio\portfolio-portrait-2.webp" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\assets\img\portfolio\portfolio-portrait-3.webp" -Force -ErrorAction SilentlyContinue
Write-Host "  [OK] Unused portfolio images removed" -ForegroundColor Green

# ── Readme / text files ───────────────────────────────────────────────────────
Remove-Item "$root\assets\scss\Readme.txt" -Force -ErrorAction SilentlyContinue
Remove-Item "$root\forms\Readme.txt" -Force -ErrorAction SilentlyContinue
Write-Host "  [OK] Readme files removed" -ForegroundColor Green

Write-Host ""
Write-Host "Done! All unused files have been deleted." -ForegroundColor Cyan
Write-Host "Press any key to close..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
