"""
Run this once on your Mac to download all images:
  python3 download_images.py
"""
import urllib.request, os

os.makedirs("images", exist_ok=True)

IMAGES = {
    # Large images
    "hero.jpg":         "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=900&auto=format&fit=crop&q=70",
    "gallery1.jpg":     "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=500&auto=format&fit=crop&q=70",
    "gallery2.jpg":     "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=500&auto=format&fit=crop&q=70",
    "gallery3.jpg":     "https://images.unsplash.com/photo-1551218808-94e220e084d2?w=500&auto=format&fit=crop&q=70",
    "gallery4.jpg":     "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=500&auto=format&fit=crop&q=70",
    "ambiance.jpg":     "https://images.unsplash.com/photo-1600565193348-f74bd3c7ccdf?w=800&auto=format&fit=crop&q=70",
    "about_hero.jpg":   "https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=1200&auto=format&fit=crop&q=70",
    "collage1.jpg":     "https://images.unsplash.com/photo-1543353071-873f17a7a088?w=600&auto=format&fit=crop&q=70",
    "collage2.jpg":     "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?w=400&auto=format&fit=crop&q=70",
    "collage3.jpg":     "https://images.unsplash.com/photo-1476224203421-9ac39bcb3327?w=400&auto=format&fit=crop&q=70",
    "collage4.jpg":     "https://images.unsplash.com/photo-1574894709920-11b28e7367e3?w=400&auto=format&fit=crop&q=70",
    "team1.jpg":        "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=400&auto=format&fit=crop&q=70",
    "team2.jpg":        "https://images.unsplash.com/photo-1607631568010-a87245c0daf8?w=400&auto=format&fit=crop&q=70",
    "team3.jpg":        "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=400&auto=format&fit=crop&q=70",
    "menu_hero.jpg":    "https://images.unsplash.com/photo-1484980972926-edee96e0960d?w=1200&auto=format&fit=crop&q=70",
    # Indian dishes
    "butter_chicken.jpg": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=200&auto=format&fit=crop&q=70",
    "biryani.jpg":        "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=200&auto=format&fit=crop&q=70",
    "dal_makhani.jpg":    "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=200&auto=format&fit=crop&q=70",
    "tandoori.jpg":       "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=200&auto=format&fit=crop&q=70",
    # Menu thumbnails
    "scallops.jpg":     "https://images.unsplash.com/photo-1534482421-64566f976cfa?w=150&auto=format&fit=crop&q=70",
    "chocolate.jpg":    "https://images.unsplash.com/photo-1551024506-0bccd828d307?w=150&auto=format&fit=crop&q=70",
    "wine.jpg":         "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=150&auto=format&fit=crop&q=70",
    "cocktail.jpg":     "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=150&auto=format&fit=crop&q=70",
    "panna_cotta.jpg":  "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=150&auto=format&fit=crop&q=70",
    "mocktail.jpg":     "https://images.unsplash.com/photo-1499638673689-79a0b5115d87?w=150&auto=format&fit=crop&q=70",
    "burrata.jpg":      "https://images.unsplash.com/photo-1608897013039-887f21d8c804?w=150&auto=format&fit=crop&q=70",
    "duck.jpg":         "https://images.unsplash.com/photo-1432139509613-5c4255815697?w=150&auto=format&fit=crop&q=70",
    "seabass.jpg":      "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=150&auto=format&fit=crop&q=70",
    "wagyu.jpg":        "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=150&auto=format&fit=crop&q=70",
    "wellington.jpg":   "https://images.unsplash.com/photo-1476224203421-9ac39bcb3327?w=150&auto=format&fit=crop&q=70",
    "cheese.jpg":       "https://images.unsplash.com/photo-1452195100486-9cc805987862?w=150&auto=format&fit=crop&q=70",
    "soup.jpg":         "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=150&auto=format&fit=crop&q=70",
    "duck_liver.jpg":   "https://images.unsplash.com/photo-1544025162-d76694265947?w=150&auto=format&fit=crop&q=70",
}

headers = {"User-Agent": "Mozilla/5.0"}
ok = 0
fail = 0
for filename, url in IMAGES.items():
    path = os.path.join("images", filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as r, open(path, "wb") as f:
            f.write(r.read())
        size = os.path.getsize(path)
        print(f"  ✓ {filename} ({size//1024}KB)")
        ok += 1
    except Exception as e:
        print(f"  ✗ {filename} — {e}")
        fail += 1

print(f"\nDone! {ok} downloaded, {fail} failed.")
print("Now open index.html in your browser — all images should load locally.")
