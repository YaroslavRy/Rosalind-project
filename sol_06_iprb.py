import os


def read_data(path):
    f = open(path)
    r = f.read()
    s = r.split()
    return s
    
def calc_prob(population):
    homo_dominant = int(population[0])
    hetero = int(population[1])
    homo_rec = int(population[2])

    total = homo_dominant + hetero + homo_rec

    # calc probability of not-dominant groups mating
    prob_het_het = (hetero / total) * (hetero - 1) / (total - 1)
    prob_homorec_homorec = (homo_rec / total) * (homo_rec - 1) / (total - 1)
    prob_het_homorec = (hetero / total) * (homo_rec / (total - 1)) + (homo_rec / total) * (hetero / (total - 1))
    
    # 0.25 and 0.5 are probabilities of offspring will be recessive. 
    # Сan be calculated using Punnett square 
    # https://en.wikipedia.org/wiki/Punnett_square
    prob_dominant = 1 - (prob_homorec_homorec + prob_het_het * 0.25 + prob_het_homorec * 0.5)
    
    print(prob_dominant)


if __name__ == '__main__':
	path_to_file = os.path.join(os.path.dirname(__file__), 'data/rosalind_iprb.txt')
	pop = read_data(path_to_file)
	calc_prob(pop)
