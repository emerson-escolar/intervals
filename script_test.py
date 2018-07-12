import mp_tools
import intervals

if __name__ == "__main__":
    data = mp_tools.get_data_in_paper()
    for x in data.keys():
        print("***********************************************************")
        print(x)
        print(data[x])
        print(mp_tools.generate_mp_matrix(x))
