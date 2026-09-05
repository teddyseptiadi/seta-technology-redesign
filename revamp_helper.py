#!/usr/bin/env python3
import os
import re

DIR = "/tmp/seta-redesign-work"

NAV_HEADER = """  <!-- TOP INDUSTRIAL HEADER -->
  <div class="border-b border-industrial-border bg-industrial-900 text-xs py-2.5 px-4 sm:px-8">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-2 font-mono text-[11px]">
      <div class="flex items-center space-x-4 text-slate-400">
        <span class="flex items-center gap-2 text-slate-200">
          <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
          PT SETA TECHNOLOGY ASIA • REKAYASA OTOMASI INDUSTRI
        </span>
        <span class="hidden md:inline text-slate-700">|</span>
        <span class="hidden md:inline text-slate-400">Grand Slipi Tower Lt. 9, Jakarta Barat</span>
      </div>
      <div class="flex items-center space-x-6 text-slate-300">
        <a href="tel:+6282213928230" class="hover:text-industrial-accent transition flex items-center gap-1.5">
          <i data-lucide="phone" class="w-3.5 h-3.5 text-industrial-accent"></i>
          <span>Hotline Teknis: <strong class="text-white font-semibold">+62 822 1392 8230</strong></span>
        </a>
        <span class="text-slate-700">|</span>
        <a href="mailto:raden@seta.co.id" class="hover:text-industrial-accent transition">raden@seta.co.id</a>
      </div>
    </div>
  </div>

  <!-- NAVIGATION -->
  <nav class="sticky top-0 z-50 bg-industrial-900/95 backdrop-blur border-b border-industrial-border">
    <div class="max-w-7xl mx-auto px-4 sm:px-8 h-20 flex items-center justify-between">
      
      <!-- LOGO -->
      <a href="index.html" class="flex items-center space-x-3.5 group">
        <div class="w-10 h-10 rounded bg-industrial-blue flex items-center justify-center font-display font-extrabold text-white text-lg tracking-wider border border-industrial-blueHover shadow-md">
          ST
        </div>
        <div>
          <div class="text-lg font-bold tracking-tight text-white font-display group-hover:text-industrial-accent transition">
            SETA <span class="text-slate-300">TECHNOLOGY</span>
          </div>
          <div class="text-[10px] tracking-widest text-slate-400 font-mono -mt-0.5 font-semibold uppercase">
            Asia • Feeding & Sorting Machinery
          </div>
        </div>
      </a>

      <!-- DESKTOP NAV -->
      <div class="hidden lg:flex items-center space-x-8 text-xs font-mono font-bold uppercase tracking-wider">
        <a href="index.html" class="{NAV_ACTIVE_HOME} transition pb-1">Home</a>
        
        <!-- PRODUCTS DROPDOWN -->
        <div class="relative group">
          <button class="flex items-center gap-1 {NAV_ACTIVE_PRODUCTS} transition py-2">
            <span>Mesin & Sistem</span>
            <i data-lucide="chevron-down" class="w-3.5 h-3.5 text-slate-500 group-hover:rotate-180 transition"></i>
          </button>
          
          <div class="absolute left-0 top-full mt-1 w-72 bg-industrial-900 border border-industrial-border rounded-xl shadow-2xl p-2 hidden group-hover:block z-50 backdrop-blur-xl">
            <a href="product.html" class="block p-3 rounded-lg hover:bg-industrial-800 transition">
              <div class="text-white font-sans font-semibold text-sm">Vibratory Bowl Feeder</div>
              <div class="text-[11px] font-sans text-slate-400 mt-0.5">Sistem orientasi part otomatis hingga 600 PPM</div>
            </a>
            <a href="product-automatic-sorting-machine.html" class="block p-3 rounded-lg hover:bg-industrial-800 transition border-t border-industrial-border/50">
              <div class="text-white font-sans font-semibold text-sm">Optical Sorting Machine</div>
              <div class="text-[11px] font-sans text-slate-400 mt-0.5">Inspeksi visual multi-kamera akurasi ±0.01 mm</div>
            </a>
            <a href="product-sorting-house.html" class="block p-3 rounded-lg hover:bg-industrial-800 transition border-t border-industrial-border/50">
              <div class="text-white font-sans font-semibold text-sm">Integrated Sorting House</div>
              <div class="text-[11px] font-sans text-slate-400 mt-0.5">Stasiun perakitan terisolasi peredam suara &lt; 70 dBA</div>
            </a>
          </div>
        </div>

        <a href="about.html" class="{NAV_ACTIVE_ABOUT} transition pb-1">Tentang Kami</a>
        <a href="download.html" class="{NAV_ACTIVE_DOWNLOAD} transition pb-1">Katalog & CAD</a>
        <a href="contact.html" class="{NAV_ACTIVE_CONTACT} transition pb-1">Kontak & RFQ</a>
      </div>

      <!-- CTA BUTTON -->
      <div class="hidden sm:flex items-center space-x-4">
        <a href="contact.html" class="px-5 py-2.5 rounded-lg bg-industrial-accent hover:bg-industrial-accentHover text-industrial-950 font-bold text-xs font-mono uppercase tracking-wider transition shadow-lg flex items-center gap-2">
          <span>Minta Penawaran (RFQ)</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>

      <!-- MOBILE MENU BUTTON -->
      <div class="lg:hidden flex items-center">
        <button id="mobile-menu-btn" class="p-2 text-slate-400 hover:text-white focus:outline-none">
          <i data-lucide="menu" class="w-6 h-6"></i>
        </button>
      </div>

    </div>

    <!-- MOBILE MENU DRAWER -->
    <div id="mobile-menu" class="lg:hidden hidden border-b border-industrial-border bg-industrial-900 px-6 py-4 space-y-3 font-mono text-sm">
      <a href="index.html" class="block text-slate-300 hover:text-white py-2">Home</a>
      <a href="product.html" class="block text-slate-300 hover:text-white py-1">Vibratory Bowl Feeder</a>
      <a href="product-automatic-sorting-machine.html" class="block text-slate-300 hover:text-white py-1">Optical Sorting Machine</a>
      <a href="product-sorting-house.html" class="block text-slate-300 hover:text-white py-1">Integrated Sorting House</a>
      <a href="about.html" class="block text-slate-300 hover:text-white py-2">Tentang Kami</a>
      <a href="download.html" class="block text-slate-300 hover:text-white py-2">Katalog & CAD</a>
      <a href="contact.html" class="block text-slate-300 hover:text-white py-2">Kontak & RFQ</a>
      <a href="contact.html" class="block w-full text-center py-3 bg-industrial-accent text-industrial-950 font-bold rounded-lg mt-2">Minta Penawaran Teknis</a>
    </div>
  </nav>"""

FOOTER = """  <!-- FOOTER -->
  <footer class="bg-industrial-950 text-slate-400 text-xs py-14 mt-auto border-t border-industrial-border">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-10 pb-12 border-b border-industrial-border">
        
        <!-- COMPANY BIO -->
        <div class="md:col-span-4 space-y-4">
          <div class="flex items-center space-x-3">
            <div class="w-8 h-8 rounded bg-industrial-blue flex items-center justify-center font-display font-extrabold text-white text-base">
              ST
            </div>
            <span class="font-display font-bold text-lg text-white">SETA TECHNOLOGY ASIA</span>
          </div>
          <p class="text-slate-400 text-xs leading-relaxed">
            Spesialis perancangan dan manufaktur Vibratory Bowl Feeder kustom, Mesin Sortir Optik Otomatis, dan Sistem Otomasi Pabrik Presisi Tinggi di Indonesia.
          </p>
          <div class="text-[11px] font-mono text-slate-500">
            Badan Hukum: PT SETA Technology Asia
          </div>
        </div>

        <!-- QUICK LINKS -->
        <div class="md:col-span-3 space-y-3 font-mono">
          <div class="text-xs font-bold text-white uppercase tracking-wider">Lini Produk</div>
          <ul class="space-y-2 text-xs">
            <li><a href="product.html" class="hover:text-industrial-accent transition">Vibratory Bowl Feeder</a></li>
            <li><a href="product-automatic-sorting-machine.html" class="hover:text-industrial-accent transition">Automatic Sorting Machine</a></li>
            <li><a href="product-sorting-house.html" class="hover:text-industrial-accent transition">Integrated Sorting House</a></li>
            <li><a href="download.html" class="hover:text-industrial-accent transition">Katalog & Lembar Data Teknis</a></li>
          </ul>
        </div>

        <!-- CORPORATE -->
        <div class="md:col-span-2 space-y-3 font-mono">
          <div class="text-xs font-bold text-white uppercase tracking-wider">Perusahaan</div>
          <ul class="space-y-2 text-xs">
            <li><a href="about.html" class="hover:text-industrial-accent transition">Tentang Kami</a></li>
            <li><a href="contact.html" class="hover:text-industrial-accent transition">Hubungi Kami</a></li>
            <li><a href="contact.html" class="hover:text-industrial-accent transition">Lokasi Workshop & Kantor</a></li>
          </ul>
        </div>

        <!-- CONTACT INFO -->
        <div class="md:col-span-3 space-y-3">
          <div class="text-xs font-mono font-bold text-white uppercase tracking-wider">Kantor Pusat Jakarta</div>
          <p class="text-xs text-slate-400 leading-relaxed">
            Grand Slipi Tower Lt. 9 Unit O, Jl. Letjen S. Parman Kav. 22–24, Palmerah, Jakarta Barat 11480.
          </p>
          <div class="space-y-1 font-mono text-xs text-slate-300">
            <div>Tel: <a href="tel:+6282213928230" class="text-white hover:text-industrial-accent font-semibold">+62 822 1392 8230</a></div>
            <div>Email: <a href="mailto:raden@seta.co.id" class="text-white hover:text-industrial-accent font-semibold">raden@seta.co.id</a></div>
          </div>
        </div>

      </div>

      <!-- COPYRIGHT -->
      <div class="pt-8 flex flex-col sm:flex-row justify-between items-center text-[11px] font-mono text-slate-500 gap-2">
        <div>&copy; 2026 PT SETA Technology Asia. All rights reserved.</div>
        <div>Rekayasa Presisi • SAK EMKM & ISO Compliance</div>
      </div>

    </div>
  </footer>

  <script>
    lucide.createIcons();
    const btn = document.getElementById('mobile-menu-btn');
    const menu = document.getElementById('mobile-menu');
    if (btn && menu) {
      btn.addEventListener('click', () => {
        menu.classList.toggle('hidden');
      });
    }
  </script>"""

HEAD_CONFIG = """  <!-- Typography: Syne, IBM Plex Sans & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">
  
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['"IBM Plex Sans"', 'sans-serif'],
            display: ['"Syne"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          },
          colors: {
            industrial: {
              950: '#070a11',
              900: '#0b0f19',
              850: '#101623',
              800: '#161e30',
              700: '#1f293d',
              border: '#243048',
              borderLight: '#334155',
              accent: '#f59e0b',
              accentHover: '#d97706',
              blue: '#2563eb',
              blueHover: '#1d4ed8',
              muted: '#94a3b8',
            }
          }
        }
      }
    }
  </script>
  <style>
    body {
      background-color: #070a11;
      color: #f8fafc;
      font-family: 'IBM Plex Sans', sans-serif;
    }
    .tabular-nums { font-variant-numeric: tabular-nums; }
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: #070a11; }
    ::-webkit-scrollbar-thumb { background: #243048; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #334155; }
  </style>"""

print("Helper templates defined.")
