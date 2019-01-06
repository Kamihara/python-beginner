import csv
import os
import pathlib

def main():

    print('********************************************')
    print('こんにちは!私はRobokoです。あなたの名前は何ですか?')
    print('********************************************')

    user_name = input()

    print('********************************************')
    print('{}さん。どこのレストランが好きですか?'.format(user_name))
    print('********************************************')

    restaurant = input()
    make_list(restaurant)

    print('********************************************')
    print('{}さん。ありがとうございました。'.format(user_name))
    print('良い一日を!さようなら。')
    print('********************************************')

def make_list(restaurant):
    fields = ['NAME', 'COUNT']

    if os.path.exists("ranking.csv"):
        pass
    else:
        pathlib.Path("ranking.csv").touch()

    with open("ranking.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        rows = reader.

    with open('ranking.csv', "w") as csvfile:
        # reader = csv.DictReader(csvfile, fieldnames=fields)
        # for row in reader:
        #     if restaurant == row['NAME']:
        #         writer.writerow({'NAME': row['NAME'], 'COUNT': row['COUNT']+1})
        #     else:
        #         writer.writerow({'NAME': restaurant, 'COUNT': 1})
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerow({
            'NAME': restaurant,
            'COUNT': 1,
        })


if __name__ == "__main__":
    main()