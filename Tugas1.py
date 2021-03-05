class student():
    def nama(self):
        print("nama    :", self.full_name)
        
    def get_age (self):
        print("umur    :", self.age)
    def get_gender (self):
        print("gender  :", self.gender)
    def get_alamat (self):
        print("alamat  :", self.alamat)
riyadh = student()

riyadh.full_name = "Riyadh Ahmad F"
riyadh.age = "20"
riyadh.gender = "Laki-laki"
riyadh.alamat = "Jakarta"

riyadh.nama()
riyadh.get_age()
riyadh.get_gender()
riyadh.get_alamat()