import sys

inputs = sys.argv
data_file = inputs[1]

# collect the data
data_dict = {'county_name':[], 'population':[], 'area':[], 'density':[]}

with open(data_file, 'r') as file:
    for line in file:
        name, _,pop, area = line.strip('\n').split(',')
        data_dict['county_name'].append(name)
        data_dict['population'].append(int(pop))
        data_dict['area'].append(float(area))
        data_dict['density'].append(float(pop)/float(area))

# analyze the data
#
# find the average of a list
def average(lst):
    return sum(lst) / len(lst)

# find standard deviation of a list
def standard_deviation(lst):
    avg = average(lst)
    second_moment = average([x**2 for x in lst])
    return (second_moment - avg**2)**0.5

# find the top 3 counties with largest population
top_3_pop = sorted(data_dict['population'], reverse=True)[:3]
top_3_pop_counties = [data_dict['county_name'][data_dict['population'].index(pop)] for pop in top_3_pop]

# find the top three counties with the largest area
top_3_area = sorted(data_dict['area'], reverse=True)[:3]
top_3_area_counties = [data_dict['county_name'][data_dict['area'].index(area)] for area in top_3_area]

# find the highest and lowest population density
highest_density = max(data_dict['density'])
lowest_density = min(data_dict['density'])
top_density_county = data_dict['county_name'][data_dict['density'].index(highest_density)]
lowest_density_county = data_dict['county_name'][data_dict['density'].index(lowest_density])

# print the results
county_pop_avg = round(average(data_dict['population']))
county_pop_std = round(standard_deviation(data_dict['population']),2)
print('\nHere are some statistics about the counties in the data file: ', "\n")
print('The average county population is: ', county_pop_avg, 'with a standard deviation of', county_pop_std,"\n" )
print('The top 3 most populous counties are: ', "\n\n")
for i in range(3):
    print('\t', i+1, '. ', top_3_pop_counties[i], 'with a population of', top_3_pop[i], "\n")
print('The top 3 largest counties by area are: ', "\n")
for i in range(3):
    print('\t', i+1, '. ', top_3_area_counties[i], 'with an area of', top_3_area[i], "\n")
print('\n')
print('The highest population density is', top_density_county, 'with a density of', highest_density, 
      'and the lowest is', lowest_density_county, 'with a density of', lowest_density, "\n")