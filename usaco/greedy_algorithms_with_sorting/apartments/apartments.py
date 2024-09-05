num_applicants, num_apartments, max_diff = map(int, input().split())
size_per_applicant = list(map(int, input().split()))
apartments = list(map(int, input().split()))

size_per_applicant.sort()
apartments.sort()
applicant = 0
apartment = 0
matched_applicants = 0
while applicant < num_applicants and apartment < num_apartments:
    if abs(apartments[apartment] - size_per_applicant[applicant]) <= max_diff:
        matched_applicants+=1
        applicant+=1
        apartment+=1
    else:
        if apartments[apartment] < size_per_applicant[applicant]: # too small
            apartment+=1
        else: # this applicant cannot be placed
            applicant+=1

print(matched_applicants)