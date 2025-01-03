1

# Bron qilingan xonalar ro'yxatini saqlash
bron_qilingan_xonalar = []

while True:
    print("\n" + "="*40)
    print(">>>  🏨 5-Yulduzli Mehmonxona Xizmatlari Menyusi  <<<")
    print("="*40)
    print("1️⃣  Xona bron qilish")
    print("2️⃣  Bron qilingan xonalar haqida ma'lumot")
    print("3️⃣  Mehmonxona haqida ma'lumot")
    print("4️⃣  Mehmonxona qulayliklari")
    print("5️⃣  Narxlar va paketlar")
    print("6️⃣  Chiqish")
    print("="*40)

    try:
        num = int(input("👉 Tanlang: "))
    except ValueError:
        print("❌ Noto'g'ri kirish. Iltimos, raqam kiriting.")
        continue

    if num == 1:  # Xona bron qilish
        print("\n>>> 🔒 Xona bron qilish")
        full_name = input("To'liq ismingizni kiriting: ").strip()
        try:
            age = int(input("Yoshingizni kiriting: "))
        except ValueError:
            print("❌ Yoshingizni to'g'ri kiriting.")
            continue

        phone = input("Telefon raqamingizni kiriting: +998 ").strip()

        if len(phone) != 9 or not phone.isdigit():
            print("❌ Telefon raqam xato. Iltimos, 9 xonali raqam kiriting.")
        elif age < 18:
            print("❌ Yoshingiz kichik, bron qilish mumkin emas.")
        else:
            family_room = input("👉 Oilaviy xona kerakmi? (ha/yo'q): ").lower()
            booked_family_room = family_room == "ha"
            if booked_family_room:
                print("✅ Oilaviy xona muvaffaqiyatli bron qilindi!")
            # bu yerda Necha kun turisiz
            try:
                days = int(input("👉 Necha kun turishni rejalashtiryapsiz? "))
                if days <= 0:
                    print("❌ Kunlar soni noto'g'ri.")
                    continue
            except ValueError:
                print("❌ Kunlar sonini to'g'ri kiriting.")
                continue

            print("\nQavatlarni tanlang:")
            print("1️⃣  1-qavat (narxi: 2 000 000 so'm) – premium to'plam")
            print("2️⃣  2-qavat (narxi: 1 800 000 so'm) – Okean manzarali xona")
            print("3️⃣  3-qavat (narxi: 1 800 000 so'm) – Shahar manzarali xona")
            print("4️⃣  4-qavat (narxi: 1 800 000 so'm) – lyuks xona")
            print("5️⃣  5-qavat (narxi: 1 600 000 so'm) – standart xona")

            try:
                # qavat tanlash 
                floor_choice = int(input("👉 Qavatni tanlang (raqamini kiriting): "))
            except ValueError:
                print("❌ Qavat raqami noto'g'ri.")
                continue
                # narxni qoshib umumiy narx soni chiqaradi
            if floor_choice in [1, 2, 3, 4, 5]:
                floor_prices = {1: 2_000_000, 2: 1_800_000, 3: 1_800_000, 4: 1_800_000, 5: 1_600_000}
                booked_price = floor_prices[floor_choice]
                total_price = booked_price * days  # Umumiy narxni hisoblash
                print(f"✅ {floor_choice}-qavat muvaffaqiyatli tanlandi!")
                print(f"💵 Bir kechadagi narxi: {booked_price:,} so'm")
                print(f"💵 Umumiy narx ({days} kun): {total_price:,} so'm")
            else:
                print("❌ Noto'g'ri qavat raqami.")
                continue
                    # xona raqamni tanlash 
            available_rooms = [f"{floor_choice}{room}" for room in range(10, 21)] 
            print(f"{floor_choice}-qavatdagi xonalar:")
            print("Xonalar:", ", ".join(available_rooms))

            room_choice = input("👉 Xona raqamini tanlang: ").strip()

            if room_choice in available_rooms:
                print(f"✅ Xona {room_choice} muvaffaqiyatli bron qilindi!")
            else:
                print("❌ Noto'g'ri xona raqami.")
                continue

            print("\nMehmonxona qulayliklari:")
            print("1️⃣  Spa va sog'lomlashtirish markazi (yoga, massaj, sauna)")
            print("2️⃣  Sport zal va fitnes markazi")
            print("3️⃣  Restoran va bar (internatsional oshxona)")
            print("4️⃣  Konferensiya xonasi va biznes markazi")
            print("5️⃣  Hovuz va akvapark")
            print("6️⃣  VIP xonalar va xususiy xizmatlar")


            subscriptions = input("👉 Qaysi qulayliklarga obuna bo'lishni xohlaysiz? (1-6, vergul bilan ajrating): ").split(",")
            available_subscriptions = {
                "1": "Spa va sog'lomlashtirish markazi",
                "2": "Sport zal va fitnes markazi",
                "3": "Restoran va bar",
                "4": "Konferensiya xonasi",
                "5": "Hovuz va akvapark",
                "6": "VIP xonalar va xususiy xizmatlar"
            }

            selected_subscriptions = [available_subscriptions[sub.strip()] for sub in subscriptions if sub.strip() in available_subscriptions]

            # Bron qilingan xona haqida ma'lumotni saqlash
            bron_qilingan_xonalar.append({
                "Ism": full_name,
                "Yosh": age,
                "Telefon": f"+998 {phone}",
                "Xona": room_choice,
                "Kunlar": days,
                "Umumiy narx": f"{total_price:,} so'm",
                "Qulayliklar": selected_subscriptions
            })

            print("\n📝 Bron qilish yakunlandi!")
            print(f"📋 Xona {room_choice} muvaffaqiyatli bron qilindi!")

    elif num == 2:  # Bron qilingan xonalar haqida ma'lumot
        if not bron_qilingan_xonalar:
            print("\n📋 Hozircha hech qanday xona bron qilinmagan.")
        else:
            print("\n📋 Bron qilingan xonalar haqida ma'lumot:")
            for idx, bron in enumerate(bron_qilingan_xonalar, start=1):
                print(f"\n{idx}. Xona: {bron['Xona']}")
                print(f"   - Ism: {bron['Ism']}")
                print(f"   - Yosh: {bron['Yosh']}")
                print(f"   - Telefon: {bron['Telefon']}")
                print(f"   - Kunlar soni: {bron['Kunlar']}")
                print(f"   - Umumiy narx: {bron['Umumiy narx']}")
                print(f"   - Qulayliklar:")
                for q in bron["Qulayliklar"]:
                    print(f"     ✔️ {q}")

    elif num == 3:
        print("\n>>> 🏢 Mehmonxonaga borish")
        print("📍 Manzil: Toshkent sh., Mustaqillik ko'chasi, 101")
        print("📞 Telefon: +998 71 123-45-67")
        print("🗺 Mo'ljal: Toshkent markazi")

    elif num == 4:
        print("\n>>> 🛌 Mehmonxona qulayliklari")
        print("- Zamonaviy mebel va konditsionerlar bilan jihozlangan")
        print("- Bepul Wi-Fi va yuqori tezlikdagi internet")
        print("- 24/7 xona xizmati va shaxsiy")
        print("- Restoran, kafelar, va barlar")
        print("- Ichki hovuz va akvapark")
        print("- Spa va sog'lomlashtirish markazi")
        print("- Sport zal va fitnes markazi")
        print("- VIP xonalar va biznes markazi")
        print("- Bepul avtoturargoh va taksi xizmati")
        print("- Elektron kutubxona, kinoteatr, va ekskursiyalar")

    elif num == 5:
        print("\n>>> 💵 Mehmonxona narxlari va paketlar")
        print("1️⃣  premium to'plam (bir kecha): 2 000 000 so'm")
        print("2️⃣  Okean manzarali xona (bir kecha): 1 800 000 so'm")
        print("3️⃣  Shahar manzarali xona (bir k  echa): 1 800 000 so'm")
        print("4️⃣  lyuks xona (bir kecha ): 1 800 000 so'm")
        print("5️⃣  standart xona (bir kecha): 1 600 000 so'm")
    elif num == 6:
        print("📤 Dasturdan chiqildi. Rahmat!")
        break

    else:
            print("❌ Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")


