if __name__ == '__main__':

    user_age = int(input('Enter your Age to determine your maximum heart rate: '))
    max_heart_rate = 220 - user_age
    print(f'Your Heart rate beats at %d' % max_heart_rate,'bpm')

    #determine the target heart based on the range 50 - 85%

    target_hrt_rate = 50 * max_heart_rate / 100
    print('Minimum Target Heart Rate: ', target_hrt_rate)
    target_hrt_rate1 = 85 * max_heart_rate / 100
    print('Maximum Target Heart Rate: ', target_hrt_rate1)

