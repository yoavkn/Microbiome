# authors: Noa Lichtenstein and Yoav Knaanie
import shutil
import time
import top20
import download
import os
import sys

CONTAM_NOTATION = ['HUMAN', 'PIG', 'BOVIN', 'SHEEP', 'YEAST']
INPUT_NUMBER = 7

if __name__ == '__main__':
    """
    directory: should contain: first_step folder, resources/fragpipe_files->
    (fragger.params, fragpipe.workflow, fragpipe-files.fp-manifest)
    first_step folder should contain raw files samples for analysing with ms fragger and Human_Top_100.fasta.
    
    creates chosen_fastas folder in directory containing the unified proteome
    creates first_step
    """
    if len(sys.argv) != INPUT_NUMBER:
        sys.exit("Invalid input. the input should be in the format: "
                 "fragpipe_directory directory raw_file_list(format: 'raw1','raw2','raw3'...) "
                 "true/false organisms_list(format example:"
                 "'Actinomyces+naeslundii','Actinomyces+oris','Corynebacterium+amycolatum'..."
                 " number_of_fastas_to_download")

    fragpipe_directory = sys.argv[1]  # The folder in which the fragpipe was installed
    directory = sys.argv[2]
    add = sys.argv[3]
    raw_list = sys.argv[4].split(',')
    organisms = sys.argv[5].replace("'", "").split(',')
    number_of_fastas_download = int(sys.argv[6])  # number of fasta files to download from Uniprot

    print(f"add == {add}")
    print(f"raw_list == {raw_list}")
    print(f"organisms == {organisms}")

    results_dir = rf"{directory}\first_step"

    start_time = time.time()
    # download only if there is no already a folder
    download.download_organisms_main(fragpipe_directory, directory, raw_list, organisms, results_dir, number_of_fastas_download)
    end_time = time.time()
    running_time = end_time - start_time
    print(f"download running time: {running_time} seconds")
    chosen_fastas_folder = rf'{directory}\chosen_fastas'
    os.mkdir(chosen_fastas_folder)

    # up until this point everything is the same
    if add == "true":
        shutil.copy(rf"{directory}\resources\fasta\combined_proteome.fasta", chosen_fastas_folder)
        shutil.copy(rf"{directory}\resources\fasta\proteins_per_bacteria.txt", chosen_fastas_folder)
    shutil.copy(rf"{directory}\resources\fasta\Human_Top_100.fasta", chosen_fastas_folder)
    # todo: should we add 100_human to the combined proteome?
    top20.top20_main_function(raw_list=raw_list, organisms=organisms, directory=results_dir,
                              chosen_fastas_folder=chosen_fastas_folder)


    # typical input
    # directory = r"C:\Users\owner\Microbiome\Building_a_Unified_Proteome"
    # raw_list = [
    #     "2022_05_25_09_PreNatal3_Sample1_S1_SCX_p2",
    #     "2022_05_25_07_PreNatal3_Sample2_S1_SCX_p2",
    #     "2022_05_25_05_PreNatal3_Sample3_S1_SCX_p2",
    #     "2022_05_25_03_PreNatal3_Sample4_S1_SCX_p2",
    #     "2022_05_25_01_PreNatal3_Sample5_S1_SCX_p2",
    #     "2021_12_10_11_PreNatal2_Sample2_S1_p2",
    #     "2021_12_10_13_PreNatal2_Sample3_S1_p2",
    #     "2021_12_10_07_PreNatal1_Sample1_S1_p2",
    #     "2021_12_10_09_PreNatal1_Sample2_S1_p2",
    #     "2021_12_10_01_PreNatal1_Sample3_S1_p2",
    #     "2021_12_10_02_PreNatal2_Sample1_S1_p2"
    # ]
    # organisms = [
    #     'Actinomyces+naeslundii',
    #     'Actinomyces+oris',
    #     'Corynebacterium+amycolatum',
    #     'Corynebacterium+striatum',
    #     'Dermabacter+hominis',
    #     'Rothia+mucilaginosa',
    #     'Cutibacterium+avidum',
    #     'Gemella+haemolysans',
    #     'Staphylococcus+epidermidis',
    #     'Staphylococcus+hominis',
    #     'Enterococcus+faecalis',
    #     'Lactobacillus+rhamnosus',
    #     'Streptococcus+infantis',
    #     'Streptococcus+salivarius',
    #     'Clostridium+perfringens',
    #     'Negativicoccus+succinicivorans',
    #     'Veillonella+atypica',
    #     'Veillonella+parvula',
    #     'Finegoldia+magna',
    #     'Citrobacter+braakii',
    #     'Citrobacter+youngae',
    #     'Enterobacter+cloacae_complex',
    #     'Escherichia+coli',
    #     'Klebsiella+aerogenes',
    #     'Klebsiella+michiganensis',
    #     'Klebsiella+oxytoca',
    #     'Klebsiella+pneumoniae',
    #     'Kluyvera+ascorbata',
    #     'Proteus+mirabilis'
    # ]
