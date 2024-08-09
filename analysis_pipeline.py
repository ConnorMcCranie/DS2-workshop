import sys
import matplotlib.pyplot as plt

# This script reads a data file and performs some basic analysis on the data.
##############################

# read the data file and store the data in a dictionary
def parse_data_file():
    """
    This function reads the data file and returns a dictionary with the data.
    The data should be in the format:
    county_name, state name, population, area
    Additionally, the function takes in three command line arguments:
    - the number of counties to display for population
    - the number of counties to display for area
    - a boolean indicating whether to display the max/min population density

    The output is a dictionary with the following
    keys: 'county_name', 'population', 'area', 'density'
    """
    # read the data file from the command line
    inputs = sys.argv
    data_file , pop_num ,area_num , display_density = inputs[1:5]

    # create a dictionary to store the data
    data_dict = {'county_name':[], 'population':[], 'area':[], 'density':[]}

    with open(data_file, 'r') as file:
        for line in file:
            name, _,pop, area = line.strip('\n').split(',')
            data_dict['county_name'].append(name)
            data_dict['population'].append(int(pop))
            data_dict['area'].append(float(area))
            data_dict['density'].append(float(pop)/float(area))
    return data_dict , int(pop_num) ,int(area_num) , bool(display_density)


# find the average of a list
def average(lst):
    return sum(lst) / len(lst)

# find standard deviation of a list
def standard_deviation(lst):
    avg = average(lst)
    second_moment = average([x**2 for x in lst])
    return (second_moment - avg**2)**0.5


# find the counties with the largest or smallest values for a given key

def get_top(data_dict, key,n=1):
    """
    This function returns the top n counties for a given key in the data dictionary.
    If n is positive, it returns the top n counties (largest values for the key).
    If n is negative, it returns the least n counties (smallest values for the key).

    """
    if n > 0 :
        most = True
    else:
        most = False
    top = sorted(data_dict[key], reverse=most)[:n]
    top_counties = [data_dict['county_name'][data_dict[key].index(pop)] for pop in top]
    if n == 1 or n == -1:
        return top[0], top_counties[0]
    else:
        return top,top_counties


#########################################

def main():
    # check if the correct number of command line arguments are provided
    if len(sys.argv) != 5:
        print('Input error. Format terminal command as \npython analysis_pipeline.py data_file pop_num area_num display_density')
    else:
        data_dict , pop_num ,area_num , display_density = parse_data_file()
        top_n_pop, top_n_pop_counties = get_top(data_dict, 'population',pop_num)
        top_n_area, top_n_area_counties = get_top(data_dict, 'area',area_num)
        top_density, top_density_county = get_top(data_dict, 'density')
        least_density, least_density_county = get_top(data_dict, 'density', -1)
        county_pop_avg = round(average(data_dict['population']))
        county_pop_std = round(standard_deviation(data_dict['population']),2)

        # print the results
        
        print('\nHere are some statistics about the counties in the data file: ', "\n")
        print('The average county population is', county_pop_avg, 'with a standard deviation of', county_pop_std,"\n" )
        
        if pop_num == 1:
            print('The most populous county is', top_n_pop_counties, 'with a population of', top_n_pop, "\n")
        else: 
            print('The top',pop_num,  'most populous counties are: ', "\n")
            for i in range(pop_num):
                print('\t', i+1, '. ', top_n_pop_counties[i], 'with a population of', top_n_pop[i], "\n")
        
        if area_num == 1:
            print('The largest county by area is', top_n_area_counties, 'with an area of', top_n_area, "\n")
        else:
            print('The top', area_num, 'largest counties by area are: ', "\n")
            for i in range(area_num):
                print('\t', i+1, '. ', top_n_area_counties[i], 'with an area of', top_n_area[i], "\n")
        if display_density == True:
            print('The highest population density is', top_density_county,
                'with a density of', round(top_density), 'people per square mile,', 
                "\n", 'and the lowest is', least_density_county, 'with a density of',
                    round(least_density), 'people per square mile.', "\n")
        
                
        # plot the data
        # plot the population of each county
        fig, ax = plt.subplots(1,2, figsize=(13,7))
        ax[0].bar(data_dict['county_name'], data_dict['population'])
        ax[0].set_title('County Population')
        ax[0].set_ylabel('Population')
        ax[0].set_xlabel('County')

        # plot the area of each county
        ax[1].bar(data_dict['county_name'], data_dict['area'])
        ax[1].set_title('County Area')
        ax[1].set_ylabel('Area (sq miles)')
        ax[1].set_xlabel('County')


        plt.show()

if __name__ == "__main__":
    main()