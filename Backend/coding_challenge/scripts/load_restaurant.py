from myapp.models import Restaurant
import csv


def run():
    with open('/home/dxuser/Desktop/CodingChallenge/Backend/data/restaurants.csv', mode='r', encoding='latin-1') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Restaurant.objects.all().delete()

        for row in reader:
            print(row)

            restaurant, _ = Restaurant.objects.get_or_create(
                restaurant_id = row[0],
                restaurant_name = row[1],
                country_code =row[2],
                city_code = row[3],
                address = row[4],
                locality = row[5],
                locality_verbose = row[6],
                longitude = row[7],
                latitude = row[8],
                cuisines = row[9],
                average_cost_for_two = row[10],
                currency = row[11],
                has_table_booking = row[12],
                has_online_delivery = row[13],
                is_delivering_now = row[14],
                switch_to_order_menu = row[15],
                price_range = row[16],
                aggregate_rating = row[17],
                rating_color = row[18],
                rating_text = row[19],
                votes = row[20]
            )



            # film = Film(title=row[0],
            #             year=row[2],
            #             genre=genre)
            # film.save()