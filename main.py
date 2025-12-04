import os

parking_lot = [] # Danh sách lưu biển số xe

def hien_thi_menu():
    print("\n--- QUẢN LÝ BÃI XE ---")
    print("1. Cho xe vào (Check-in)")
    print("2. Cho xe ra (Check-out)")
    print("3. Xem danh sách xe")
    print("4. Thoát")

def main():
    while True:
        hien_thi_menu()
        choice = input("Chọn chức năng (1-4): ")

        if choice == '1':
            print("Chức năng Check-in đang phát triển...")
        elif choice == '2':
            print("Chức năng Check-out đang phát triển...")
        elif choice == '3':
            print("Danh sách xe hiện tại:", parking_lot)
        elif choice == '4':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()