import random

class ATM:
    def __init__(self, user_name, bank_name, amount):
        self.user_name = user_name
        self.bank_name = bank_name
        self.amount = amount
        self.current_otp = None
        self.pending_amount = 0

    def check_balance(self):
        print(f"Your balance is {self.amount} THB")

    def deposit(self, saving):
        self.amount += saving
        print(f"Deposit {saving} THB successfully")

    def withdraw(self, saving):
        if self.amount >= saving:
            self.amount -= saving
            print(f"Withdraw {saving} THB successfully")
        else:
            print("Insufficient balance")

    def transfer(self, target_account, transfer_amount):
        if self.amount >= transfer_amount:
            self.amount -= transfer_amount
            target_account.amount += transfer_amount
            print(f"Transfer {transfer_amount} THB to {target_account.user_name} successfully.")
        else:
            print("Error: Insufficient balance.")

    def top_up_for_others(self, target_account, amount):
        if self.amount >= amount:
            self.amount -= amount
            target_account.deposit(amount)
            print(f"Top-up successfully from {self.user_name} to {target_account.user_name}")
        else:
            print("Error: Balance not enough.")

    def request_cardless_withdraw(self, amount):
        if self.amount >= amount:
            self.current_otp = str(random.randint(100000, 999999))
            self.pending_amount = amount
            print(f"OTP for {amount} THB is: {self.current_otp}")
        else:
            print("Error: Insufficient balance.")

    def verify_otp_at_atm(self, input_otp):
        # 1. เช็คว่ามีการขอ OTP ไว้จริงไหม
        if self.current_otp is None:
            print("Error: No pending request.")
            return

        # 2. เช็ครหัส (แปลงเป็น string ทั้งคู่เพื่อกันพลาด)
        if str(input_otp) == self.current_otp:
            self.amount -= self.pending_amount
            print("--- ATM ---")
            print(f"Verified! Take your cash: {self.pending_amount} THB")

            # 3. รีเซ็ตค่าหลังจากทำรายการสำเร็จ
            self.current_otp = None
            self.pending_amount = 0
        else:
            print("Error: Invalid OTP. Please try again.")