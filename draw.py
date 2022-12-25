# blog-cyberworm.com
# Bu program ile 3 adet kitaptan oluşan bir kitap seti ve 10$ çekilişi gerçekleştirdik.
# Kodun açıklaması sitede mevcut: https://blog-cyberworm.com/blog/200-blog-ozel-cekilisi-cekilis-uygulamasi

import random

# Üyeleri bir listeye giriyoruz.
members = ["A", "B", "C", "D", "E", "F", "G"]

# members isimli listenin uzunluğu kadar bir sayı listesi oluşturduk.
# Çıktı şuna benzer bir yapıda olacaktır:
# Çıktı: [0, 1, 2, 3, 4, 5, 6]
numbers = [member for member in range(len(members))]

# Listeyi karıştırıyoruz.
random.shuffle(members)

# numbers listesinden rastgele bir sayı çektik.
selectedIndex = random.choice(numbers)

#İşleyişi görmek isterseniz yazdırabilirsiniz.
"""print(f"Üyeler: {members}")
print(f"Seçilen index: {selectedIndex}")"""

# Kazananı belirliyoruz.
print(f"Kazanan: {members[selectedIndex]}")

