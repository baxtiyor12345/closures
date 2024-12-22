import time
def get_summ(*args):
    time.sleep(2)
    return sum(args)
def time_counter(funk,*args,**kwargs):
    start_time = time.time()
    print("Funksiya boshlandi ")
    result = funk(*args,**kwargs)
    end_time = time.time()
    print("Funksiya tugadi")
    counter_time = end_time - start_time
    print(f"Funksiya {counter_time} soniyada bajarildi. ")
    return result

print("Natija:", time_counter(get_summ, 1, 2, 3, 4, 5, 6, 7))