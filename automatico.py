from faker import Faker


fake = Faker("pt_BR")
seq = []

def inputar(n):

    for _ in range(n):

        seq.append(fake.name())
        seq.append(int(fake.random_int(min=18,max = 80)))
        seq.append(fake.msisdn()[:11])
    return seq