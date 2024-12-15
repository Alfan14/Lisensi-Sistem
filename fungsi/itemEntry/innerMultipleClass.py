class TypeLicense:
    def __init__(self):
        self.by       = self.LmsBy()
        self.by_sa    = self.LmsBySa()
        self.by_nc    = self.LmsByNc()
        self.by_nc_sa = self.LmsByNcSa()
        self.by_nd    = self.LmsByNd()
        self.by_nc_nd = self.LmsByNcNd()
    def show(self):
        print('LMS') 
    class LmsBy:
        def __init__(self):
            self.type ="LMS-BY"
            self.desc = 'credit must be given to the creator.'
            self.by = True
            self.sa = False
            self.nc = False
            self.nd = False
        
        def display(self):
            type  = self.type 
            desc  = self.desc
            by    = self.by
            by_sa = self.sa
            by_nc = self.nc
            by_nd = self.nd
            return type, desc ,by , by_sa , by_nc , by_nd
        def get(self):
            type  = self.type 
            desc  = self.desc
            by    = self.by
            sa = self.sa
            nc = self.nc
            nd = self.nd
            return type, desc ,by , sa , nc , nd
    class LmsBySa:
        def __init__(self):
            self.type = 'LMS-BY-SA'
            self.desc = 'BY: credit must be given to the creator.SA:Adaptations must be shared under the same terms.'
            self.by = True
            self.sa = True
            self.nc = False
            self.nd = False

        def display(self):
            print("Type :", self.type )
            print("Description :", self.desc ) 
            print("Aktive BY", self.by)
            print("Aktive SA", self.sa)
            print("Aktive NC", self.nc)
            print("Aktive ND", self.nd)
        def get(self):
            type  = self.type 
            desc  = self.desc
            by    = self.by
            sa = self.sa
            nc = self.nc
            nd = self.nd
            return type, desc ,by , sa , nc , nd
    class LmsByNc:
        def __init__(self):
            self.type = "LMS-BY-NC"
            self.desc = 'BY : credit must be given to the creator.NC : Only noncommercial uses of the work are permitted.'
            self.by = True
            self.sa = False
            self.nc = True
            self.nd = False

        def display(self):
            print("Type :", self.type )
            print("Description :", self.desc ) 
            print("Aktive BY", self.by)
            print("Aktive SA", self.sa)
            print("Aktive NC", self.nc)
            print("Aktive ND", self.nd)
            
        def get(self):
            type  = self.type 
            desc  = self.desc
            by    = self.by
            sa = self.sa
            nc = self.nc
            nd = self.nd
            return type, desc ,by , sa , nc , nd
    class LmsByNcSa:
        def __init__(self):
            self.type = "LMS-BY-NC-SA"
            self.desc = 'BY : credit must be given to the creator.SA : Adaptations must be shared under the same terms.\nNC : Only noncommercial uses of the work are permitted.'
            self.by = True
            self.sa = True
            self.nc = True
            self.nd = False

        def display(self):
            print("Type =", self.type )
            print("Description :", self.desc ) 
            print("NC:", self.nc_desc)
            print("Aktive BY", self.by)
            print("Aktive SA", self.sa)
            print("Aktive NC", self.nc)
            print("Aktive ND", self.nd)
        def get(self):
            type  = self.type 
            desc  = self.desc
            by    = self.by
            sa = self.sa
            nc = self.nc
            nd = self.nd
            return type, desc ,by , sa , nc , nd
    class LmsByNd:
        def __init__(self):
            self.type = "LMS-BY-ND"
            self.desc = 'BY : credit must be given to the creator.ND : No derivatives or adaptations of the work are permitted.'
            self.by = True
            self.sa = False
            self.nc = False
            self.nd = True

        def display(self):
            print("Type =", self.type )
            print("Description :", self.desc ) 
            print("Aktive BY", self.by)
            print("Aktive SA", self.sa)
            print("Aktive NC", self.nc)
            print("Aktive ND", self.nd)
            
        def get(self):
            type  = self.type 
            desc  = self.desc
            by    = self.by
            sa = self.sa
            nc = self.nc
            nd = self.nd
            return type, desc ,by , sa , nc , nd
    class LmsByNcNd:
        def __init__(self):
            self.type = "LMS-BY-NC-ND"
            self.desc = 'BY : credit must be given to the creator.NC : Only noncommercial uses of the work are permitted.ND : No derivatives or adaptations of the work are permitted.'
            self.by = True
            self.sa = False
            self.nc = True
            self.nd = True

        def display(self):
            print("Type =", self.type )
            print("Description =", self.desc ) 
            print("ND:", self.nd_desc)
            print("Aktive BY", self.by)
            print("Aktive SA", self.sa)
            print("Aktive NC", self.nc)
            print("Aktive ND", self.nd)
        
        def get(self):
            type  = self.type 
            desc  = self.desc
            by    = self.by
            sa = self.sa
            nc = self.nc
            nd = self.nd
            return type, desc ,by , sa , nc , nd
def license_main(new):
    # of outer class
    outer = TypeLicense()

    # of 1st inner class
    c1 = outer.by

    # of 2nd inner class
    c2 = outer.by_sa

    # of 3rd inner class
    c3 = outer.by_nc

    # of 4th inner class
    c4 = outer.by_nc_sa

    # of 5th inner class
    c5 = outer.by_nd

    # of 6th inner class
    c6 = outer.by_nc_nd

    print("Hore berhasil memilih Lisensi")
    if new == 1:
        return c1.get()
    elif new == 2:
        return c2.get()
    elif new == 3:
        return c3.get()
    elif new == 4:
        return c4.get()
    elif new == 5:
        return c5.get()
    elif new == 6:
        return c6.get()
    else:
        return None

    

