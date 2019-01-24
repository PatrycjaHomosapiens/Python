print(f"normalna treść do wyświetlenia {2+4}")

a = [1,2,3,4]
liczba_pi = 3.1415
dl_reprezentacji = 15
print(f"normalna treść {a} do wyświetlenia {2+4}\n"
      f"{liczba_pi: .2f}\n"      # f jak float, jak tylko będzie ".2" to oznacza cyfrę znaczącą
      f"#{liczba_pi:^10}#\n"    
      f"{liczba_pi: >10}\n"      
      f"#{liczba_pi:@=10.2f}#\n"    
      f"#{liczba_pi:^{dl_reprezentacji}.2f}#\n")