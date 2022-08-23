def build_car(manu, model, **kargs):
    kargs['manufacturer'] = manu
    kargs['model'] = model
    return kargs

car_profile = build_car('Audi', 'A4 TDI Ultra', color = 'Black', body = 'state', year = '2017')
#print(user_profile)
for key, value in car_profile.items():
    print(f"- {key}: {value}")
print("\n")
print(car_profile)
