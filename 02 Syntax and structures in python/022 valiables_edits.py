if __name__ == '__main__':

    # 2.2.14 solution
    required_nodes = 68796
    mb_requred = 30
    gb_per_pod = 16
    level_1 = 4
    level_2 = 117
    level_3 = 21

    dc_count = int(required_nodes/(level_1 * level_2 * level_3))
    mb_lost = level_3 * dc_count * \
        ((gb_per_pod * 1024) - (level_1 * level_2 * mb_requred))
    gb = mb_lost//1024
    left_mb = mb_lost % 1024
    result_string = ",".join(
        [str(dc_count), str(mb_lost), str(gb), str(left_mb)])
    print('result')
    print(result_string)
