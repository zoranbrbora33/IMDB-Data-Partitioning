# %%
def main():
    from landing import get_partitions
    from datalake import convert_to_csv
    from move_files import move_files

    get_partitions()
    convert_to_csv()
    move_files()
    
if __name__ == "__main__":
    main()

# %%
