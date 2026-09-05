#!/usr/bin/env python3
import os

DIR = "/tmp/seta-redesign-work"

def get_header(title, desc):
    return f"""<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | PT SETA Technology Asia</title>
  <meta name="description" content="{desc}">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
  
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"IBM Plex Sans"', 'sans-serif'],
            display: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          }},
          colors: {{
            corporate: {{
              50: '#f8fafc',
              100: '#f1f5f9',
              200: '#e2e8f0',
              300: '#cbd5e1',
              400: '#94a3b8',
              500: '#64748b',
              600: '#475569',
              700: '#334155',
              800: '#1e293b',
              900: '#0f172a',
              primary: '#0284c7',
              primaryHover: '#0369a1',
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    body {{
      background-color: #f8fafc;
      color: #1e293b;
      font-family: 'IBM Plex Sans', sans-serif;
    }}
    .tabular-nums {{ font-variant-numeric: tabular-nums; }}
  </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased flex flex-col min-h-screen">"""

def get_nav(active_page):
    def act(name):
        return "text-corporate-primary border-b-2 border-corporate-primary pb-1" if name == active_page else "text-slate-700 hover:text-corporate-primary transition"

    return f"""  <!-- TOP BAR -->
  <div class="border-b border-slate-200 bg-white text-xs py-2.5 px-4 sm:px-8">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-2 text-[12px] text-slate-600 font-sans">
      <div class="flex items-center space-x-3">
        <span class="font-semibold text-slate-900">PT SETA Technology Asia</span>
        <span class="text-slate-300">|</span>
        <span>Spesialis Otomasi Feeding & Sorting Industri</span>
      </div>
      <div class="flex items-center space-x-6 text-slate-600">
        <a href="tel:+6282213928230" class="hover:text-corporate-primary transition flex items-center gap-1.5 font-medium">
          <i data-lucide="phone" class="w-3.5 h-3.5 text-corporate-primary"></i>
          <span>Hubungi Tim Sales: <strong>+62 822 1392 8230</strong></span>
        </a>
        <span class="text-slate-300">|</span>
        <a href="mailto:raden@seta.co.id" class="hover:text-corporate-primary transition">raden@seta.co.id</a>
      </div>
    </div>
  </div>

  <!-- NAVIGATION -->
  <nav class="sticky top-0 z-50 bg-white/95 backdrop-blur border-b border-slate-200 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-8 h-20 flex items-center justify-between">
      <a href="index.html" class="flex items-center space-x-3.5 group">
        <div class="w-10 h-10 rounded-lg bg-corporate-primary flex items-center justify-center font-display font-extrabold text-white text-lg tracking-wider shadow-sm">
          ST
        </div>
        <div>
          <div class="text-lg font-bold tracking-tight text-slate-900 font-display">
            SETA <span class="text-corporate-primary">TECHNOLOGY</span>
          </div>
          <div class="text-[11px] tracking-wider text-slate-500 font-sans font-medium uppercase">
            Asia • Automation Machinery
          </div>
        </div>
      </a>

      <div class="hidden lg:flex items-center space-x-8 text-sm font-sans font-semibold">
        <a href="index.html" class="{act('home')}">Beranda</a>
        
        <div class="relative group">
          <button class="flex items-center gap-1 text-slate-700 hover:text-corporate-primary transition py-2">
            <span>Produk & Mesin</span>
            <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 group-hover:rotate-180 transition"></i>
          </button>
          
          <div class="absolute left-0 top-full mt-1 w-80 bg-white border border-slate-200 rounded-xl shadow-xl p-2 hidden group-hover:block z-50">
            <a href="product.html" class="block p-3 rounded-lg hover:bg-slate-50 transition">
              <div class="text-slate-900 font-semibold text-sm">Vibratory Bowl Feeder</div>
              <div class="text-xs text-slate-500 mt-0.5">Sistem pengumpan part otomatis hingga 600 PPM</div>
            </a>
            <a href="product-automatic-sorting-machine.html" class="block p-3 rounded-lg hover:bg-slate-50 transition border-t border-slate-100">
              <div class="text-slate-900 font-semibold text-sm">Optical Sorting Machine</div>
              <div class="text-xs text-slate-500 mt-0.5">Inspeksi visual optik dengan akurasi ±0.01 mm</div>
            </a>
            <a href="product-sorting-house.html" class="block p-3 rounded-lg hover:bg-slate-50 transition border-t border-slate-100">
              <div class="text-slate-900 font-semibold text-sm">Integrated Sorting House</div>
              <div class="text-xs text-slate-500 mt-0.5">Kabin stasiun perakitan kedap suara &lt; 70 dBA</div>
            </a>
          </div>
        </div>

        <a href="about.html" class="{act('about')}">Tentang Kami</a>
        <a href="download.html" class="{act('download')}">Katalog & CAD</a>
        <a href="contact.html" class="{act('contact')}">Kontak & RFQ</a>
      </div>

      <div class="hidden sm:flex items-center space-x-4">
        <a href="contact.html" class="px-5 py-2.5 rounded-lg bg-corporate-primary hover:bg-corporate-primaryHover text-white font-semibold text-sm transition shadow-sm flex items-center gap-2">
          <span>Minta Penawaran (RFQ)</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </a>
      </div>

      <div class="lg:hidden flex items-center">
        <button id="mobile-menu-btn" class="p-2 text-slate-600 hover:text-slate-900">
          <i data-lucide="menu" class="w-6 h-6"></i>
        </button>
      </div>
    </div>

    <div id="mobile-menu" class="lg:hidden hidden border-b border-slate-200 bg-white px-6 py-4 space-y-3 text-sm font-medium">
      <a href="index.html" class="block text-slate-700 hover:text-corporate-primary py-1">Beranda</a>
      <a href="product.html" class="block text-slate-700 hover:text-corporate-primary py-1">Vibratory Bowl Feeder</a>
      <a href="product-automatic-sorting-machine.html" class="block text-slate-700 hover:text-corporate-primary py-1">Optical Sorting Machine</a>
      <a href="product-sorting-house.html" class="block text-slate-700 hover:text-corporate-primary py-1">Integrated Sorting House</a>
      <a href="about.html" class="block text-slate-700 hover:text-corporate-primary py-1">Tentang Kami</a>
      <a href="download.html" class="block text-slate-700 hover:text-corporate-primary py-1">Katalog & CAD</a>
      <a href="contact.html" class="block text-slate-700 hover:text-corporate-primary py-1">Kontak & RFQ</a>
    </div>
  </nav>"""

def get_footer():
    return """  <!-- FOOTER -->
  <footer class="bg-white text-slate-600 text-xs py-14 mt-auto border-t border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-10 pb-12 border-b border-slate-200">
        
        <div class="md:col-span-4 space-y-4">
          <div class="flex items-center space-x-3">
            <div class="w-8 h-8 rounded bg-corporate-primary flex items-center justify-center font-display font-extrabold text-white text-base">
              ST
            </div>
            <span class="font-display font-bold text-lg text-slate-900">SETA TECHNOLOGY ASIA</span>
          </div>
          <p class="text-slate-500 text-xs leading-relaxed">
            Perancangan dan manufaktur Vibratory Bowl Feeder kustom, Mesin Sortir Optik Otomatis, dan Sistem Otomasi Pabrik Presisi Tinggi di Indonesia.
          </p>
          <div class="text-[11px] text-slate-400">
            PT SETA Technology Asia • Jakarta Barat
          </div>
        </div>

        <div class="md:col-span-3 space-y-3 font-sans">
          <div class="text-xs font-bold text-slate-900 uppercase tracking-wider">Lini Produk</div>
          <ul class="space-y-2 text-xs">
            <li><a href="product.html" class="hover:text-corporate-primary transition">Vibratory Bowl Feeder</a></li>
            <li><a href="product-automatic-sorting-machine.html" class="hover:text-corporate-primary transition">Automatic Sorting Machine</a></li>
            <li><a href="product-sorting-house.html" class="hover:text-corporate-primary transition">Integrated Sorting House</a></li>
            <li><a href="download.html" class="hover:text-corporate-primary transition">Katalog & Lembar Data Teknis</a></li>
          </ul>
        </div>

        <div class="md:col-span-2 space-y-3 font-sans">
          <div class="text-xs font-bold text-slate-900 uppercase tracking-wider">Perusahaan</div>
          <ul class="space-y-2 text-xs">
            <li><a href="about.html" class="hover:text-corporate-primary transition">Tentang Kami</a></li>
            <li><a href="contact.html" class="hover:text-corporate-primary transition">Hubungi Kami</a></li>
            <li><a href="contact.html" class="hover:text-corporate-primary transition">Lokasi Kantor</a></li>
          </ul>
        </div>

        <div class="md:col-span-3 space-y-3">
          <div class="text-xs font-bold text-slate-900 uppercase tracking-wider">Kantor Pusat Jakarta</div>
          <p class="text-xs text-slate-500 leading-relaxed">
            Grand Slipi Tower Lt. 9 Unit O, Jl. Letjen S. Parman Kav. 22–24, Palmerah, Jakarta Barat 11480.
          </p>
          <div class="space-y-1 text-xs text-slate-600">
            <div>Tel: <a href="tel:+6282213928230" class="text-slate-900 hover:text-corporate-primary font-semibold">+62 822 1392 8230</a></div>
            <div>Email: <a href="mailto:raden@seta.co.id" class="text-slate-900 hover:text-corporate-primary font-semibold">raden@seta.co.id</a></div>
          </div>
        </div>

      </div>

      <div class="pt-8 flex flex-col sm:flex-row justify-between items-center text-[11px] text-slate-500 gap-2">
        <div>&copy; 2026 PT SETA Technology Asia. All rights reserved.</div>
        <div>Standar Mutu Rekayasa Industri Presisi</div>
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
  </script>
</body>
</html>"""

# 2. ABOUT.HTML
about_body = f"""{get_header('Tentang Kami & Profil Rekayasa', 'Profil rekayasa industri, visi manufaktur, workshop fasilitas, dan komitmen mutu PT SETA Technology Asia di Indonesia.')}
{get_nav('about')}

  <section class="py-16 bg-white border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="max-w-3xl space-y-4">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-100 border border-slate-200 text-xs font-semibold text-corporate-primary">
          PROFIL PERUSAHAAN & STANDAR KUALITAS
        </div>
        <h1 class="font-display text-4xl sm:text-5xl font-bold text-slate-900 leading-tight">
          Rekayasa Otomasi Presisi untuk Efisiensi Manufaktur Masa Depan.
        </h1>
        <p class="text-slate-600 text-base sm:text-lg leading-relaxed">
          PT SETA Technology Asia berkomitmen memajukan efisiensi lini produksi di Indonesia melalui teknologi pengumpan mangkuk getar (*vibratory bowl feeder*) kustom dan mesin sortir optik otomatis berstandar internasional.
        </p>
      </div>
    </div>
  </section>

  <section class="py-20 bg-slate-50 border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
        <div class="space-y-6">
          <div class="text-xs font-bold text-corporate-primary uppercase tracking-wider">Komitmen Teknis</div>
          <h2 class="font-display text-3xl font-bold text-slate-900">
            Dari Desain CAD 3D Hingga Integrasi di Pabrik Anda
          </h2>
          <p class="text-slate-600 text-sm leading-relaxed">
            Setiap komponen manufaktur memiliki karakteristik unik: dimensi, pusat gravitasi, dan kecepatan aliran. Kami tidak menjual mesin generik; setiap unit dibuat kustom berdasarkan sampel part fisik aktual dari lini perakitan Anda.
          </p>
          <div class="space-y-3 pt-2">
            <div class="flex items-start gap-3">
              <div class="w-6 h-6 rounded bg-emerald-50 border border-emerald-200 flex items-center justify-center text-emerald-600 mt-0.5">
                <i data-lucide="check" class="w-4 h-4"></i>
              </div>
              <div>
                <strong class="text-slate-900 text-sm font-semibold">Uji Kelayakan Sampel Part 100%:</strong>
                <p class="text-xs text-slate-600 mt-0.5">Validasi kestabilan orientasi dan throughput sebelum produksi unit dimulai.</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <div class="w-6 h-6 rounded bg-emerald-50 border border-emerald-200 flex items-center justify-center text-emerald-600 mt-0.5">
                <i data-lucide="check" class="w-4 h-4"></i>
              </div>
              <div>
                <strong class="text-slate-900 text-sm font-semibold">Integrasi PLC Industri Standar:</strong>
                <p class="text-xs text-slate-600 mt-0.5">Kompatibel penuh dengan arsitektur PLC Omron, Siemens, Mitsubishi, dan Beckhoff.</p>
              </div>
            </div>
            <div class="flex items-start gap-3">
              <div class="w-6 h-6 rounded bg-emerald-50 border border-emerald-200 flex items-center justify-center text-emerald-600 mt-0.5">
                <i data-lucide="check" class="w-4 h-4"></i>
              </div>
              <div>
                <strong class="text-slate-900 text-sm font-semibold">Dukungan Garansi & Servis Lokal:</strong>
                <p class="text-xs text-slate-600 mt-0.5">Teknisi ahli siap memberikan bantuan instalasi, training operator, dan servis berkala.</p>
              </div>
            </div>
          </div>
        </div>

        <div class="rounded-2xl bg-white border border-slate-200 p-8 shadow-sm space-y-6">
          <h3 class="text-base font-bold text-slate-900 border-b border-slate-100 pb-3">Standar Kualitas & Material</h3>
          <div class="grid grid-cols-2 gap-4 text-xs">
            <div class="p-3.5 rounded-lg bg-slate-50 border border-slate-200">
              <span class="text-slate-500 font-medium">Material Mangkuk:</span>
              <div class="text-slate-900 font-bold mt-1">Stainless Steel SUS304</div>
            </div>
            <div class="p-3.5 rounded-lg bg-slate-50 border border-slate-200">
              <span class="text-slate-500 font-medium">Lapisan Permukaan:</span>
              <div class="text-slate-900 font-bold mt-1">Polyurethane / Teflon</div>
            </div>
            <div class="p-3.5 rounded-lg bg-slate-50 border border-slate-200">
              <span class="text-slate-500 font-medium">Elektromagnetik Drive:</span>
              <div class="text-slate-900 font-bold mt-1">Dual/Triple Coils 50Hz</div>
            </div>
            <div class="p-3.5 rounded-lg bg-slate-50 border border-slate-200">
              <span class="text-slate-500 font-medium">Tingkat Kebisingan:</span>
              <div class="text-emerald-600 font-bold mt-1">&lt; 70 dB(A) Certified</div>
            </div>
          </div>
          <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-600 leading-relaxed italic">
            "Misi kami adalah menghadirkan solusi otomasi yang andal, tahan lama, dan mampu beroperasi tanpa henti di lingkungan pabrik terberat sekalipun."
          </div>
        </div>
      </div>
    </div>
  </section>

{get_footer()}"""

with open(f"{DIR}/about.html", "w") as f:
    f.write(about_body)

# 3. PRODUCT.HTML
product_body = f"""{get_header('Vibratory Bowl Feeder Systems', 'Spesifikasi teknis Vibratory Bowl Feeder kustom presisi tinggi untuk lini perakitan otomatis hingga 600 PPM.')}
{get_nav('product')}

  <section class="py-16 bg-white border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-100 border border-slate-200 text-xs font-semibold text-corporate-primary">
            SERI ST-VBF • CUSTOM BOWL FEEDER
          </div>
          <h1 class="font-display text-4xl sm:text-5xl font-bold text-slate-900 leading-tight">
            Vibratory Bowl Feeder Kustom untuk Lini Perakitan Otomatis.
          </h1>
          <p class="text-base sm:text-lg text-slate-600 leading-relaxed">
            Sistem mangkuk getar yang dirancang secara individual untuk memisahkan, menyortir arah/orientasi, dan mengalirkan komponen secara presisi hingga kecepatan <strong class="text-slate-900">600 parts per menit</strong>.
          </p>

          <div class="grid grid-cols-3 gap-4 pt-2 max-w-lg text-xs">
            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
              <span class="text-slate-500 font-medium">Diameter Bowl:</span>
              <div class="text-slate-900 font-bold mt-1 text-sm">150 – 900 mm</div>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
              <span class="text-slate-500 font-medium">Kapasitas Umpan:</span>
              <div class="text-emerald-600 font-bold mt-1 text-sm">Hingga 600 PPM</div>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
              <span class="text-slate-500 font-medium">Tingkat Suara:</span>
              <div class="text-slate-900 font-bold mt-1 text-sm">&lt; 70 dB(A)</div>
            </div>
          </div>

          <div class="pt-4 flex flex-wrap gap-4">
            <a href="contact.html" class="px-6 py-3.5 rounded-lg bg-corporate-primary hover:bg-corporate-primaryHover text-white font-semibold text-sm transition shadow-md">
              Kirim Sampel Part untuk Uji Feeder
            </a>
            <a href="download.html" class="px-6 py-3.5 rounded-lg bg-white hover:bg-slate-50 text-slate-700 border border-slate-300 font-semibold text-sm transition flex items-center gap-2">
              <i data-lucide="download" class="w-4 h-4 text-corporate-primary"></i>
              <span>Download Datasheet ST-VBF</span>
            </a>
          </div>
        </div>

        <div class="lg:col-span-5">
          <div class="rounded-2xl bg-slate-50 border border-slate-200 p-6 shadow-sm flex items-center justify-center">
            <img src="assets/bowl-feeder-1.png" alt="Vibratory Bowl Feeder" class="max-h-80 object-contain">
          </div>
        </div>

      </div>
    </div>
  </section>

  <section class="py-20 bg-slate-50 border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <div class="max-w-2xl mb-14">
        <div class="text-xs font-bold text-corporate-primary uppercase tracking-wider mb-2">Anatomi & Komponen Utama</div>
        <h2 class="font-display text-3xl font-bold text-slate-900">
          Dirancang untuk Ketahanan Operasional 24/7
        </h2>
        <p class="text-slate-600 text-sm mt-3">
          Setiap unit dirakit menggunakan material bersertifikasi industri untuk meminimalkan gesekan dan aus pada komponen part Anda.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-3">
          <div class="w-10 h-10 rounded-lg bg-slate-100 flex items-center justify-center text-corporate-primary font-bold text-sm">01</div>
          <h3 class="font-display text-lg font-bold text-slate-900">Mangkuk Kustom (Precision Bowl)</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Dibuat dari Stainless Steel SUS304 berkualitas tinggi atau Aluminium 6061-T6. Track spiral dipahat presisi dan dilapisi Polyurethane untuk melindungi permukaan part sensitif.
          </p>
        </div>

        <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-3">
          <div class="w-10 h-10 rounded-lg bg-slate-100 flex items-center justify-center text-corporate-primary font-bold text-sm">02</div>
          <h3 class="font-display text-lg font-bold text-slate-900">Drive Unit Elektromagnetik</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Unit penggerak getar ganda/tiga koil dengan pegas daun komposit fiberglass. Menghasilkan getaran harmonik stabil dengan konsumsi energi yang sangat hemat (100–500W).
          </p>
        </div>

        <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-3">
          <div class="w-10 h-10 rounded-lg bg-slate-100 flex items-center justify-center text-corporate-primary font-bold text-sm">03</div>
          <h3 class="font-display text-lg font-bold text-slate-900">Linear Feeder & Bulk Hopper</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Jalur transfer linier dengan sensor optik penumpukan part (*track full sensor*) dan bulk hopper otomatis untuk menjaga pasokan part dalam mangkuk getar selalu konstan.
          </p>
        </div>

      </div>

    </div>
  </section>

{get_footer()}"""

with open(f"{DIR}/product.html", "w") as f:
    f.write(product_body)

# 4. PRODUCT-AUTOMATIC-SORTING-MACHINE.HTML
sorting_machine_body = f"""{get_header('Automatic Optical Sorting Machine (PSG Series)', 'Mesin sortir optik otomatis PSG Series dengan kamera resolusi tinggi untuk deteksi cacat dimensi baut, fastener, dan komponen presisi hingga 800 PPM.')}
{get_nav('product-automatic-sorting-machine.html')}

  <section class="py-16 bg-white border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-100 border border-slate-200 text-xs font-semibold text-corporate-primary">
            SERI PSG • MULTI-CAMERA OPTICAL INSPECTION
          </div>
          <h1 class="font-display text-4xl sm:text-5xl font-bold text-slate-900 leading-tight">
            Mesin Sortir Optik Otomatis Presisi Tinggi.
          </h1>
          <p class="text-base sm:text-lg text-slate-600 leading-relaxed">
            Solusi inspeksi cacat 100% menggunakan kamera optik multi-sudut untuk mendeteksi kecacatan ulir baut, dimensi kepala fastener, retak mikro, dan partikel kontaminasi pada kecepatan hingga <strong class="text-slate-900">800 parts per menit</strong>.
          </p>

          <div class="grid grid-cols-3 gap-4 pt-2 max-w-lg text-xs">
            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
              <span class="text-slate-500 font-medium">Kecepatan Sortir:</span>
              <div class="text-emerald-600 font-bold mt-1 text-sm">Hingga 800 PPM</div>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
              <span class="text-slate-500 font-medium">Akurasi Deteksi:</span>
              <div class="text-slate-900 font-bold mt-1 text-sm">±0.01 mm</div>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
              <span class="text-slate-500 font-medium">Kamera Sensor:</span>
              <div class="text-slate-900 font-bold mt-1 text-sm">1 – 6 Unit CCD</div>
            </div>
          </div>

          <div class="pt-4 flex flex-wrap gap-4">
            <a href="contact.html" class="px-6 py-3.5 rounded-lg bg-corporate-primary hover:bg-corporate-primaryHover text-white font-semibold text-sm transition shadow-md">
              Konsultasi Uji Sampel Part
            </a>
            <a href="download.html" class="px-6 py-3.5 rounded-lg bg-white hover:bg-slate-50 text-slate-700 border border-slate-300 font-semibold text-sm transition flex items-center gap-2">
              <i data-lucide="download" class="w-4 h-4 text-corporate-primary"></i>
              <span>Download Brosur PSG Sorter</span>
            </a>
          </div>
        </div>

        <div class="lg:col-span-5">
          <div class="rounded-2xl bg-slate-50 border border-slate-200 p-6 shadow-sm flex items-center justify-center">
            <img src="assets/automatic-sorting-machine-1.png" alt="Automatic Sorting Machine" class="max-h-80 object-contain">
          </div>
        </div>

      </div>
    </div>
  </section>

  <section class="py-20 bg-slate-50 border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <div class="max-w-2xl mb-14">
        <div class="text-xs font-bold text-corporate-primary uppercase tracking-wider mb-2">Kapabilitas Sistem</div>
        <h2 class="font-display text-3xl font-bold text-slate-900">
          Pemeriksaan Mutu Kualitas Tanpa Kompromi
        </h2>
        <p class="text-slate-600 text-sm mt-3">
          Menggabungkan meja putar kaca transparan (*glass disc*) dan pencahayaan strobe LED berkecepatan tinggi untuk mengambil gambar 360 derajat secara instan.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-3">
          <div class="w-10 h-10 rounded-lg bg-slate-100 flex items-center justify-center text-corporate-primary font-bold text-sm">01</div>
          <h3 class="font-display text-lg font-bold text-slate-900">Glass Plate Turntable</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Piringan kaca optik dengan transmisi cahaya tinggi memungkinkan kamera menangkap siluet tampak atas, bawah, dan samping secara simultan dalam 1 putaran.
          </p>
        </div>

        <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-3">
          <div class="w-10 h-10 rounded-lg bg-slate-100 flex items-center justify-center text-corporate-primary font-bold text-sm">02</div>
          <h3 class="font-display text-lg font-bold text-slate-900">Algoritma Machine Vision</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Software inspeksi mandiri dengan pengukuran toleransi otomatis: diameter ulir, panjang total, sudut bevel, kerataan kepala baut, dan cacat burr.
          </p>
        </div>

        <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-3">
          <div class="w-10 h-10 rounded-lg bg-slate-100 flex items-center justify-center text-corporate-primary font-bold text-sm">03</div>
          <h3 class="font-display text-lg font-bold text-slate-900">Pneumatic Ejector Cepat</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Solenoid valve berkecepatan tinggi menembakkan semburan udara presisi untuk membuang part NG (*No Good*) ke bin terpisah tanpa memperlambat siklus part OK.
          </p>
        </div>

      </div>

    </div>
  </section>

{get_footer()}"""

with open(f"{DIR}/product-automatic-sorting-machine.html", "w") as f:
    f.write(sorting_machine_body)

# 5. PRODUCT-SORTING-HOUSE.HTML
sorting_house_body = f"""{get_header('Integrated Sorting House Systems', 'Kabin stasiun perakitan terintegrasi dengan peredam suara kurang dari 70 dBA, proteksi debu, dan integrasi hopper otomatis.')}
{get_nav('product-sorting-house.html')}

  <section class="py-16 bg-white border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-100 border border-slate-200 text-xs font-semibold text-corporate-primary">
            SERI ST-SH • MODULAR SOUNDPROOF ENCLOSURE
          </div>
          <h1 class="font-display text-4xl sm:text-5xl font-bold text-slate-900 leading-tight">
            Integrated Sorting House & Acoustic Enclosure.
          </h1>
          <p class="text-base sm:text-lg text-slate-600 leading-relaxed">
            Stasiun kerja kompak terisolasi yang menggabungkan mangkuk getar, elevator hopper, stasiun sortir kamera, dan peredam kebisingan pabrik hingga <strong class="text-slate-900">&lt; 70 dB(A)</strong> sesuai standar K3 lingkungan kerja industri.
          </p>

          <div class="grid grid-cols-3 gap-4 pt-2 max-w-lg text-xs">
            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
              <span class="text-slate-500 font-medium">Insulasi Suara:</span>
              <div class="text-emerald-600 font-bold mt-1 text-sm">&lt; 70 dB(A)</div>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
              <span class="text-slate-500 font-medium">Proteksi Debu:</span>
              <div class="text-slate-900 font-bold mt-1 text-sm">IP54 Sealed</div>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
              <span class="text-slate-500 font-medium">Akses Pintu:</span>
              <div class="text-slate-900 font-bold mt-1 text-sm">Akrilik 360°</div>
            </div>
          </div>

          <div class="pt-4 flex flex-wrap gap-4">
            <a href="contact.html" class="px-6 py-3.5 rounded-lg bg-corporate-primary hover:bg-corporate-primaryHover text-white font-semibold text-sm transition shadow-md">
              Konsultasi Desain Enclosure
            </a>
            <a href="download.html" class="px-6 py-3.5 rounded-lg bg-white hover:bg-slate-50 text-slate-700 border border-slate-300 font-semibold text-sm transition flex items-center gap-2">
              <i data-lucide="download" class="w-4 h-4 text-corporate-primary"></i>
              <span>Download Spesifikasi Sorting House</span>
            </a>
          </div>
        </div>

        <div class="lg:col-span-5">
          <div class="rounded-2xl bg-slate-50 border border-slate-200 p-6 shadow-sm flex items-center justify-center">
            <img src="assets/sorting-house-1.png" alt="Integrated Sorting House" class="max-h-80 object-contain">
          </div>
        </div>

      </div>
    </div>
  </section>

  <section class="py-20 bg-slate-50 border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <div class="max-w-2xl mb-14">
        <div class="text-xs font-bold text-corporate-primary uppercase tracking-wider mb-2">Keunggulan Desain Modular</div>
        <h2 class="font-display text-3xl font-bold text-slate-900">
          Lingkungan Kerja Bersih, Aman, dan Senyap
        </h2>
        <p class="text-slate-600 text-sm mt-3">
          Mengurangi polusi suara getaran logam berat di area produksi sekaligus melindungi sensor optik presisi dari debu lingkungan pabrik.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-3">
          <div class="w-10 h-10 rounded-lg bg-slate-100 flex items-center justify-center text-corporate-primary font-bold text-sm">01</div>
          <h3 class="font-display text-lg font-bold text-slate-900">Busa Akustik Densitas Tinggi</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Dinding kabin dilapisi material penyerap suara bersertifikasi tahan api (*flame retardant*) yang efektif meredam benturan getaran part logam.
          </p>
        </div>

        <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-3">
          <div class="w-10 h-10 rounded-lg bg-slate-100 flex items-center justify-center text-corporate-primary font-bold text-sm">02</div>
          <h3 class="font-display text-lg font-bold text-slate-900">Struktur Aluminium Profil Heavy Duty</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Rangka aluminium anodized kokoh dengan kaki peredam getaran (*leveling anti-vibration pads*) dan roda pengunci untuk kemudahan relokasi layout.
          </p>
        </div>

        <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-3">
          <div class="w-10 h-10 rounded-lg bg-slate-100 flex items-center justify-center text-corporate-primary font-bold text-sm">03</div>
          <h3 class="font-display text-lg font-bold text-slate-900">Panel Kontrol Sentral HMI</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Satu layar sentuh HMI terpasang di sisi luar kabin untuk memantau kecepatan feeding, statistik part cacat, level hopper, dan saklar emergency stop.
          </p>
        </div>

      </div>

    </div>
  </section>

{get_footer()}"""

with open(f"{DIR}/product-sorting-house.html", "w") as f:
    f.write(sorting_house_body)

# 6. DOWNLOAD.HTML
download_body = f"""{get_header('Pusat Unduhan Brosur & Data Teknis CAD', 'Download katalog produk, datasheet spesifikasi teknis, dan formulir permintaan file 3D CAD STEP.')}
{get_nav('download')}

  <section class="py-16 bg-white border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      <div class="max-w-3xl space-y-4">
        <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-100 border border-slate-200 text-xs font-semibold text-corporate-primary">
          DOKUMENTASI TEKNIS & PUSAT CAD 3D
        </div>
        <h1 class="font-display text-4xl sm:text-5xl font-bold text-slate-900 leading-tight">
          Pusat Unduhan Brosur & Data Teknis CAD.
        </h1>
        <p class="text-slate-600 text-base sm:text-lg leading-relaxed">
          Dapatkan akses langsung ke lembar spesifikasi teknis PDF, diagram dimensi pemasangan, dan pengajuan file 3D CAD (.STEP) untuk kebutuhan simulasi rekayasa mesin Anda.
        </p>
      </div>
    </div>
  </section>

  <section class="py-20 bg-slate-50 border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm flex flex-col justify-between">
          <div class="space-y-4">
            <div class="w-12 h-12 rounded-xl bg-slate-100 flex items-center justify-center text-corporate-primary">
              <i data-lucide="file-text" class="w-6 h-6"></i>
            </div>
            <div>
              <span class="text-xs text-slate-400 font-medium">PDF • 4.2 MB • Versi 2026</span>
              <h3 class="font-display text-lg font-bold text-slate-900 mt-1">Katalog Produk Utama 2026</h3>
            </div>
            <p class="text-xs text-slate-600 leading-relaxed">
              Katalog komprehensif seluruh lini Vibratory Bowl Feeder, Linear Feeder, Optical Sorter, dan Sorting House beserta tabel matriks pemilihan tipe.
            </p>
          </div>
          <div class="mt-8 pt-4 border-t border-slate-100">
            <a href="assets/catalog-seta-2026.pdf" download class="w-full py-2.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-800 font-semibold text-xs border border-slate-200 transition flex items-center justify-center gap-2">
              <i data-lucide="download" class="w-4 h-4 text-corporate-primary"></i>
              <span>Download Katalog PDF</span>
            </a>
          </div>
        </div>

        <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm flex flex-col justify-between">
          <div class="space-y-4">
            <div class="w-12 h-12 rounded-xl bg-slate-100 flex items-center justify-center text-corporate-primary">
              <i data-lucide="cpu" class="w-6 h-6"></i>
            </div>
            <div>
              <span class="text-xs text-slate-400 font-medium">PDF • 2.8 MB • Rev 1.4</span>
              <h3 class="font-display text-lg font-bold text-slate-900 mt-1">Datasheet Seri PSG Sorter</h3>
            </div>
            <p class="text-xs text-slate-600 leading-relaxed">
              Lembar data teknis mendalam mengenai sistem kamera inspeksi, resolusi lensa optik, diagram kelistrikan I/O PLC, dan spesifikasi udara pneumatik.
            </p>
          </div>
          <div class="mt-8 pt-4 border-t border-slate-100">
            <a href="assets/datasheet-psg-series.pdf" download class="w-full py-2.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-800 font-semibold text-xs border border-slate-200 transition flex items-center justify-center gap-2">
              <i data-lucide="download" class="w-4 h-4 text-corporate-primary"></i>
              <span>Download Datasheet PDF</span>
            </a>
          </div>
        </div>

        <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm flex flex-col justify-between">
          <div class="space-y-4">
            <div class="w-12 h-12 rounded-xl bg-slate-100 flex items-center justify-center text-emerald-600">
              <i data-lucide="box" class="w-6 h-6"></i>
            </div>
            <div>
              <span class="text-xs text-emerald-600 font-semibold">CAD 3D Model (.STEP)</span>
              <h3 class="font-display text-lg font-bold text-slate-900 mt-1">Request File CAD 3D (.STEP)</h3>
            </div>
            <p class="text-xs text-slate-600 leading-relaxed">
              Memerlukan file model 3D untuk disimulasikan ke dalam rancangan layout mesin pabrik Anda? Kirimkan spesifikasi envelope dimensi yang diinginkan.
            </p>
          </div>
          <div class="mt-8 pt-4 border-t border-slate-100">
            <a href="contact.html?type=cad_request" class="w-full py-2.5 rounded-lg bg-corporate-primary hover:bg-corporate-primaryHover text-white font-semibold text-xs transition flex items-center justify-center gap-2 shadow-sm">
              <span>Minta File CAD 3D</span>
              <i data-lucide="arrow-right" class="w-4 h-4"></i>
            </a>
          </div>
        </div>

      </div>

    </div>
  </section>

{get_footer()}"""

with open(f"{DIR}/download.html", "w") as f:
    f.write(download_body)

# 7. CONTACT.HTML
contact_body = f"""{get_header('Kontak & Permintaan Penawaran (RFQ)', 'Hubungi tim engineering PT SETA Technology Asia untuk permintaan penawaran harga (RFQ), konsultasi sampel part, dan jadwal kunjungan workshop.')}
{get_nav('contact')}

  <section class="py-16 bg-white border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
        
        <div class="lg:col-span-5 space-y-8">
          <div>
            <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-100 border border-slate-200 text-xs font-semibold text-corporate-primary mb-3">
              KANTOR PUSAT & WORKSHOP
            </div>
            <h1 class="font-display text-3xl sm:text-4xl font-bold text-slate-900 leading-tight">
              Konsultasikan Kebutuhan Feeding & Sorting Pabrik Anda.
            </h1>
            <p class="text-slate-600 text-sm mt-3 leading-relaxed">
              Tim aplikasi teknik kami siap membantu menganalisis sampel part, merancang konsep orientasi mangkuk, dan menyusun penawaran harga resmi (RFQ) dalam waktu 1x24 jam kerja.
            </p>
          </div>

          <div class="space-y-4">
            
            <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
              <div class="flex items-center gap-2.5 text-xs text-corporate-primary font-bold uppercase">
                <i data-lucide="map-pin" class="w-4 h-4"></i>
                <span>Alamat Kantor Pusat</span>
              </div>
              <p class="text-xs text-slate-700 leading-relaxed font-sans">
                <strong>PT SETA Technology Asia</strong><br>
                Grand Slipi Tower Lt. 9 Unit O, Jl. Letjen S. Parman Kav. 22–24, Palmerah, Jakarta Barat 11480, Indonesia.
              </p>
            </div>

            <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
              <div class="flex items-center gap-2.5 text-xs text-corporate-primary font-bold uppercase">
                <i data-lucide="phone" class="w-4 h-4"></i>
                <span>Kontak & WhatsApp Bisnis</span>
              </div>
              <div class="text-xs space-y-1 font-sans">
                <div>Direct Line: <a href="tel:+6282213928230" class="text-slate-900 hover:text-corporate-primary font-bold">+62 822 1392 8230</a></div>
                <div>Technical Email: <a href="mailto:raden@seta.co.id" class="text-slate-900 hover:text-corporate-primary font-bold">raden@seta.co.id</a></div>
              </div>
            </div>

            <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
              <div class="flex items-center gap-2.5 text-xs text-emerald-700 font-bold uppercase">
                <i data-lucide="clock" class="w-4 h-4"></i>
                <span>Jam Operasional Engineering</span>
              </div>
              <div class="text-xs text-slate-600 space-y-0.5 font-sans">
                <div>Senin – Jumat: 08:00 – 17:00 WIB</div>
                <div>Layanan Emergency Support: 24/7 (Sesuai Kontrak SLA)</div>
              </div>
            </div>

          </div>
        </div>

        <div class="lg:col-span-7">
          <div class="rounded-2xl bg-white border border-slate-200 p-8 shadow-sm space-y-6">
            <div class="border-b border-slate-100 pb-4">
              <h2 class="font-display text-xl font-bold text-slate-900">Formulir Permintaan Penawaran Teknis (RFQ)</h2>
              <p class="text-xs text-slate-500 mt-1">Lengkapi rincian komponen Anda untuk respon cepat dari spesialis aplikasi kami.</p>
            </div>

            <form id="rfq-form" onsubmit="event.preventDefault(); alert('Terima kasih! Permintaan penawaran teknis Anda telah tercatat. Tim engineering kami akan menghubungi dalam 1x24 jam.');" class="space-y-4 text-xs font-sans">
              
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div class="space-y-1.5">
                  <label class="text-slate-700 font-semibold">Nama Lengkap *</label>
                  <input type="text" required placeholder="Contoh: Budi Santoso" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-slate-900 focus:outline-none focus:border-corporate-primary font-sans">
                </div>
                <div class="space-y-1.5">
                  <label class="text-slate-700 font-semibold">Nama Perusahaan / PT *</label>
                  <input type="text" required placeholder="Contoh: PT Manufaktur Otomotif Jaya" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-slate-900 focus:outline-none focus:border-corporate-primary font-sans">
                </div>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div class="space-y-1.5">
                  <label class="text-slate-700 font-semibold">Email Perusahaan *</label>
                  <input type="email" required placeholder="budi@perusahaan.co.id" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-slate-900 focus:outline-none focus:border-corporate-primary font-sans">
                </div>
                <div class="space-y-1.5">
                  <label class="text-slate-700 font-semibold">Nomor Telepon / WhatsApp *</label>
                  <input type="tel" required placeholder="08123456789" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-slate-900 focus:outline-none focus:border-corporate-primary font-sans">
                </div>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div class="space-y-1.5">
                  <label class="text-slate-700 font-semibold">Jenis Mesin yang Dibutuhkan *</label>
                  <select class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-slate-900 focus:outline-none focus:border-corporate-primary font-sans">
                    <option>Vibratory Bowl Feeder (Custom System)</option>
                    <option>Optical Sorting Machine (PSG Series)</option>
                    <option>Integrated Sorting House (Soundproof Enclosure)</option>
                    <option>Linear Feeder & Bulk Hopper Saja</option>
                    <option>Permintaan File 3D CAD (.STEP)</option>
                  </select>
                </div>
                <div class="space-y-1.5">
                  <label class="text-slate-700 font-semibold">Target Kecepatan (PPM)</label>
                  <input type="text" placeholder="Contoh: 300 pcs/menit" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3.5 py-2.5 text-slate-900 focus:outline-none focus:border-corporate-primary font-sans">
                </div>
              </div>

              <div class="space-y-1.5">
                <label class="text-slate-700 font-semibold">Deskripsi & Dimensi Part (Material, Panjang x Lebar x Tinggi, Bobot) *</label>
                <textarea rows="4" required placeholder="Jelaskan jenis part (misal: baut flange M6x20 SUS304), orientasi akhir yang diinginkan, dan kendala lini saat ini..." class="w-full bg-slate-50 border border-slate-300 rounded-lg p-3 text-slate-900 focus:outline-none focus:border-corporate-primary font-sans leading-relaxed"></textarea>
              </div>

              <button type="submit" class="w-full py-3.5 rounded-lg bg-corporate-primary hover:bg-corporate-primaryHover text-white font-semibold text-sm transition shadow-md mt-2 flex items-center justify-center gap-2">
                <span>Kirim Permintaan Penawaran (RFQ)</span>
                <i data-lucide="send" class="w-4 h-4"></i>
              </button>

            </form>

          </div>
        </div>

      </div>

    </div>
  </section>

{get_footer()}"""

with open(f"{DIR}/contact.html", "w") as f:
    f.write(contact_body)

print("ALL 7 PAGES COMPILED TO CLEAN CORPORATE B2B LIGHT THEME SUCCESSFULLY.")
