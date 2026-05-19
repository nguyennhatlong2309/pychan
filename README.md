# 🍄 PyChan — Mario Game in Python

> Một game Mario fan-made được xây dựng hoàn toàn bằng **Python** và **Pygame**, tái hiện lại trải nghiệm platformer cổ điển với 3 màn chơi, hệ thống kẻ thù đa dạng, âm thanh và hiệu ứng đầy đủ.

---

## 📋 Mục Lục

- [Giới thiệu](#-giới-thiệu)
- [Tính năng](#-tính-năng)
- [Công nghệ sử dụng](#-công-nghệ-sử-dụng)
- [Cấu trúc thư mục](#-cấu-trúc-thư-mục)
- [Hướng dẫn cài đặt](#-hướng-dẫn-cài-đặt)
- [Cách chơi](#-cách-chơi)
- [Nhân vật &amp; Kẻ thù](#-nhân-vật--kẻ-thù)
- [Hệ thống vật phẩm](#-hệ-thống-vật-phẩm)
- [Tác giả](#-tác-giả)

---

## 🎮 Giới thiệu

**PyChan** là một dự án cá nhân được phát triển nhằm tái tạo trải nghiệm chơi game Mario kinh điển. Game bao gồm **3 màn chơi** với độ khó tăng dần, hệ thống camera cuộn ngang, các loại kẻ thù thông minh, vật phẩm tăng sức mạnh, và hệ thống tính điểm có lưu trữ lịch sử.

---

## ✨ Tính năng

### Gameplay

- ✅ **3 màn chơi** với bối cảnh khác nhau (overworld, platform, dungeon)
- ✅ **Camera cuộn ngang** mượt mà, tự động theo nhân vật
- ✅ **Hệ thống trọng lực & vật lý** — nhảy cao/thấp tùy lực nhấn
- ✅ **Pause game** bất cứ lúc nào bằng phím `P`
- ✅ **Blink (invincibility)** — kỹ năng tránh đòn tạm thời bằng phím `V`
- ✅ **Bắn fireball** ở màn 3 với số đạn giới hạn

### Giao diện

- ✅ **Menu chính** với nền game đẹp mắt và điều hướng bằng bàn phím
- ✅ **HUD đầy đủ** — Điểm, Xu, Thế giới, Thời gian, Mạng, Blink, Đạn
- ✅ **Màn hình Game Over & Win** với overlay đẹp
- ✅ **Bảng điểm cao** (High Score) có thanh cuộn

### Âm thanh

- ✅ Nhạc nền riêng cho menu, gameplay và game over
- ✅ Hiệu ứng âm thanh cho mọi hành động: nhảy, thu xu, chết, nâng cấp, bắn đạn, phá gạch...

---

## 🛠️ Công nghệ sử dụng

| Thành phần               | Chi tiết                      |
| -------------------------- | ------------------------------ |
| **Ngôn ngữ**       | Python 3.10+                   |
| **Game Engine**      | [Pygame](https://www.pygame.org/) |
| **Âm thanh**        | `pygame.mixer`               |
| **Font**             | Press Start 2P (Google Fonts)  |
| **Lưu trữ điểm** | File văn bản (`score.txt`) |

---

## 📁 Cấu trúc thư mục

```
pychan/
└── mario/
    ├── menu.py             # Màn hình menu chính — điểm khởi đầu của game
    ├── core.py             # Vòng lặp game, logic các màn, PAUSE, GAME OVER, WIN
    ├── game_assets.py      # Toàn bộ các class: Mario, kẻ thù, địa hình, vật phẩm
    ├── map.py              # Thiết kế 3 màn chơi (map1, map2, map3)
    ├── sounds.py           # Quản lý âm thanh (Sound, Theme)
    ├── score.txt           # Lưu trữ lịch sử điểm cao
    ├── fonts/
    │   └── PressStart2P-Regular (1).ttf
    ├── images/             # Toàn bộ sprites (Mario, kẻ thù, địa hình, vật phẩm...)
    └── sounds/             # Toàn bộ file âm thanh .mp3
```

---

## 🚀 Hướng dẫn cài đặt

### Yêu cầu hệ thống

- Python **3.10** trở lên
- pip

### Bước 1: Clone repository

```bash
git clone https://github.com/<your-username>/pychan.git
cd pychan/mario
```

### Bước 2: Cài đặt thư viện

```bash
pip install pygame
```

### Bước 3: Chạy game

```bash
python menu.py
```

> ⚠️ **Lưu ý:** Phải chạy từ thư mục `mario/` để game tìm đúng đường dẫn đến `images/`, `sounds/`, `fonts/`.

---

## 🕹️ Cách chơi

### Điều khiển

| Phím                      | Hành động                                       |
| -------------------------- | -------------------------------------------------- |
| `←` / `A`             | Di chuyển sang trái                              |
| `→` / `D`             | Di chuyển sang phải                              |
| `↑` / `W` / `Space` | Nhảy (giữ lâu = nhảy cao hơn)                 |
| `V`                      | Kích hoạt Blink (miễn nhiễm đòn tạm thời)  |
| `Z` / `X`              | Bắn fireball (chỉ ở màn 3 khi có Fire Flower) |
| `P`                      | Tạm dừng / Tiếp tục game                       |
| `↑` / `↓`            | Điều hướng menu                                |
| `Enter`                  | Chọn trong menu                                   |

### Mục tiêu

- Vượt qua 3 màn chơi để giành chiến thắng
- Thu thập xu để tăng điểm
- Tiêu diệt kẻ thù bằng cách nhảy lên đầu hoặc dùng fireball
- Giữ mạng và đạt điểm cao nhất

### Các chỉ số trên HUD

| Chỉ số        | Ý nghĩa                                  |
| --------------- | ------------------------------------------ |
| **SCORE** | Điểm hiện tại                          |
| **COINS** | Số xu đã thu thập                      |
| **WORLD** | Màn hiện tại (1-1, 1-2, 1-3)            |
| **TIME**  | Thời gian còn lại                       |
| **LIVES** | Số mạng còn lại                        |
| **BLINK** | Thời gian còn lại của hiệu ứng Blink |
| **AMMO**  | Số đạn fireball còn lại               |

---

## 👾 Nhân vật & Kẻ thù

### Mario (3 trạng thái)

| Trạng thái          | Mô tả                                     |
| --------------------- | ------------------------------------------- |
| **Small Mario** | Trạng thái mặc định, 1 đòn là chết |
| **Super Mario** | Nhận Super Mushroom, có thể phá gạch   |
| **Fire Mario**  | Nhận Fire Flower, bắn được fireball    |

### Kẻ thù

| Kẻ thù                          | Đặc điểm                                                  |
| --------------------------------- | ------------------------------------------------------------- |
| **Goomba**                  | Di chuyển qua lại, bị tiêu diệt khi bị nhảy lên đầu |
| **Koopa Troopa** (xanh)     | Có mai rùa, khi bị nhảy lên biến thành mai trượt     |
| **Koopa Paratroopa** (xanh) | Phiên bản có cánh của Koopa Troopa                       |
| **Red Koopa Troopa**        | Không đi ra ngoài viền bệ, hung hăng hơn               |
| **Red Koopa Paratroopa**    | Phiên bản có cánh của Red Koopa                          |
| **Hammer Brother**          | Ném búa liên tục, di chuyển theo cụm                    |
| **Piranha Plant**           | Ẩn trong ống, thò lên xuống theo chu kỳ                 |

---

## 💎 Hệ thống vật phẩm

| Vật phẩm               | Nguồn gốc                           | Hiệu ứng             |
| ------------------------ | ------------------------------------- | ---------------------- |
| **Coin**           | Question Block (loại 1)              | +1 xu, +điểm         |
| **Static Coin**    | Đặt cố định trên map            | +1 xu                  |
| **Super Mushroom** | Question Block (loại 2, Small Mario) | Nâng lên Super Mario |
| **Fire Flower**    | Question Block (loại 2, Super Mario) | Nâng lên Fire Mario  |

### Địa hình đặc biệt

- **Question Block** (`?`) — Ẩn chứa xu hoặc vật phẩm, biến thành Empty Block sau khi dùng hết
- **Brick** — Có thể phá vỡ khi là Super Mario
- **Pipe** — Trang trí, chứa Piranha Plant
- **Moving Platform** — Bệ di chuyển ngang/dọc ở màn 2
- **Gold Flag** — Cột cờ cuối màn, chạm vào để qua màn tiếp

---

## 👤 Tác giả

**Nguyễn Nhật Long**

- 🎓 Sinh viên — HK1 2025–2026
- 🔗 GitHub: [nguyennhatlong2309](https://github.com/nguyennhatlong2309)
- 📦 Repository: `nguyennhatlong2309/pychan`

---

## 📄 Giấy phép

Dự án này được thực hiện cho mục đích học tập cá nhân.
Các sprites và âm thanh được lấy từ tài nguyên công khai của cộng đồng Mario fan-made.

---

> *"It's-a me, Mario!"* 🍄
