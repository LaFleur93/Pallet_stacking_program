from math import ceil

def distribute_brondby(ts_thyme, ts_coriander, ts_rosemary, ts_mint, ts_sage, ts_tarragon, ts_basil, ts_dill, fp_basil, fp_parsley, fp_coriander, fp_mint, fp_thyme, fp_rosemary, fp_tarragon):

    ranges_trayseal = [(18,27),(36,54),(60,72),(84,120),(120,1000)]
    ranges_flowpack = [(14,24),(32,48),(56,72),(80,96),(104,120),(128,144),(152,168)]

    pallet_height, fp_height, ts_height = 0.150, 0.203, 0.303

    brondby = [("TS","Thyme",int(ts_thyme)),("TS","Flat Coriander",int(ts_coriander)),("TS","Rosemary",int(ts_rosemary)),("TS","Green Mint",int(ts_mint)),("TS","Sage",int(ts_sage)),("TS","Tarragon",int(ts_tarragon)),("TS","Italian Basil",int(ts_basil)),("TS","Dill",int(ts_dill)),("FP","Italian Basil",int(fp_basil)),("FP","Curly Parsley",int(fp_parsley)),("FP","Flat Coriander",int(fp_coriander)),("FP","Green Mint",int(fp_mint)),("FP","Thyme",int(fp_thyme)),("FP","Rosemary",int(fp_rosemary)),("FP","Tarragon",int(fp_tarragon))]

    def divide_pallet(distribution_center):
        i = 0
        for (a,b,c) in distribution_center:
            if c > 168:
                first_pallet_height = ceil(c/(2*24))*24
                second_pallet_height = c - first_pallet_height
                distribution_center.pop(i)
                distribution_center.append((a,b,first_pallet_height))
                distribution_center.append((a,b,second_pallet_height))
            i += 1
        return distribution_center

    brondby = divide_pallet(brondby)

    def trayseal_check(boxes):
        return any(lower <= boxes <= upper for (lower,upper) in ranges_trayseal)

    def flowpack_check(boxes):
        return any(lower <= boxes <= upper for (lower,upper) in ranges_flowpack)

    flat_pallets, flat_pallets_heights = [], []
    non_flat_pallets, non_flat_pallets_heights = [], []

    for variety in brondby:
        if variety[2] != 0:
            if variety[0] == "TS":    
                if trayseal_check(variety[2]):
                    height = pallet_height + ceil(variety[2]/27)*ts_height + 0.001
                    flat_pallets_heights.append(height)
                    flat_pallets.append((str(height), [variety[0] + " " + str(variety[2]) + " boxes"]))
                else:
                    height = pallet_height + ceil(variety[2]/27)*ts_height
                    non_flat_pallets_heights.append(height)
                    non_flat_pallets.append((str(height), [variety[0] + " " + str(variety[2]) + " boxes"]))
            else:     
                if flowpack_check(variety[2]):
                    height = pallet_height + ceil(variety[2]/24)*fp_height + 0.001
                    flat_pallets_heights.append(height)
                    flat_pallets.append((str(height), [variety[0] + " " + str(variety[2]) + " boxes"]))
                else:
                    height = pallet_height + ceil(variety[2]/24)*fp_height
                    non_flat_pallets_heights.append(height)
                    non_flat_pallets.append((str(height), [variety[0] + " " + str(variety[2]) + " boxes"]))

    def sorted_k_partitions(seq, k):
        n = len(seq)
        groups = []

        def generate_partitions(i):
            if i >= n:
                yield list(map(tuple, groups))
            else:
                if n - i > k - len(groups):
                    for group in groups:
                        group.append(seq[i])
                        yield from generate_partitions(i + 1)
                        group.pop()

                if len(groups) < k:
                    groups.append([seq[i]])
                    yield from generate_partitions(i + 1)
                    groups.pop()
        result = generate_partitions(0)
        #result = sorted(result, key = lambda ps: (*map(len, ps), ps))
        return result

    def check_column(columns):
        max_height = 2.10
        for column in columns:
            c = 0
            if sum(column) > max_height:
                    return False
            for pallet in column:
                if pallet in non_flat_pallets_heights:
                    c += 1
                if c > 1:
                    return False
        return True

    max_non_flat = None

    count = 0
    if 0 <= len(non_flat_pallets_heights) < 4:
        positions_needed = 4
    elif 4 <= len(non_flat_pallets_heights) <= 5:
        positions_needed = len(non_flat_pallets_heights)
    elif len(non_flat_pallets_heights) == 6:
        max_non_flat = non_flat_pallets_heights.pop(non_flat_pallets_heights.index(max(non_flat_pallets_heights)))
        positions_needed = 5
    else:
        positions_needed = 6

    #flat_pallets_heights.sort(reverse=True)
    all_heights = flat_pallets_heights + non_flat_pallets_heights

    last = ''
    while count == 0:
        generator = sorted_k_partitions(all_heights, positions_needed)
        for i in generator:
            if str(i) != last:  
                if check_column(i):
                    optim_pallets_distrib = i
                    count = 1
                    if max_non_flat != None:
                        optim_pallets_distrib.append((max_non_flat,))
                    break
            last = str(i)
        positions_needed += 1
        if positions_needed > 6:
            break

    def determine_heights(pallets):
        order_list = []
        i = {}
        for k, s in pallets:
            if k not in i:
                order_list.append((k, s))
                i[k] = len(i)
            else:
                order_list[i[k]][1].extend(s)
        return dict(order_list)

    pallets_dict = determine_heights(flat_pallets + non_flat_pallets)

    def set_heights(distribution, dictionary):
        final = [[] for n in range(len(distribution))]
        i = 0
        for column in distribution:
            for pallet in column:
                final[i].append(pallet)
                final[i].append(dictionary[str(pallet)])
            i += 1
        return final

    final_distribution = set_heights(optim_pallets_distrib, pallets_dict)
    return final_distribution

    