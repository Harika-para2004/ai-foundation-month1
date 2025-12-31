def bayes_theorem(prior, likelihood, evidence):
    """
    Docstring for bayes_theorem
    
    :param prior: Description
    :param likelihood: Description
    :param evidence: Description
    """
    return prior * likelihood / evidence

# Given
prior = 0.01          # 1% have disease
likelihood = 0.99     # test is positive if disease exists
false_positive = 0.01 # test positive when no disease

# P(E) = P(E|H)P(H) + P(E|¬H)P(¬H)
evidence = (0.99 * prior) + (false_positive * (1 - prior))

posterior = bayes_theorem(prior, likelihood, evidence)
print("Probability of having disease given positive test:", posterior)


#1
def bayes_positive(disease_rate, sensitivity, false_positive):
    numerator = sensitivity * disease_rate
    denominator = numerator + false_positive * (1 - disease_rate)
    return numerator / denominator

print(bayes_positive(0.01, 0.99, 0.05))

#2
def update_belief(prior, likelihood):
    return (prior * likelihood) / ((prior * likelihood) + (1 - prior) * (1 - likelihood))

print(update_belief(0.5, 0.9))

#3
spam_rate = 0.4
spam_detected = 0.9
false_flag = 0.1

prob_spam = (spam_rate * spam_detected) / (
    spam_rate * spam_detected + (1 - spam_rate) * false_flag
)

print(prob_spam)

#4
bagA_red = 0.9
bagB_red = 0.1

posterior_A = bagA_red / (bagA_red + bagB_red)
print(posterior_A)

#5
rain_rate = 0.1
cloud_given_rain = 0.8
cloud_given_no_rain = 0.3

prob_rain = (cloud_given_rain * rain_rate) / (
    cloud_given_rain * rain_rate + cloud_given_no_rain * (1 - rain_rate)
)

print(prob_rain)

#6
prior = 0.01
sensitivity = 0.99
false_positive = 0.05

for _ in range(2):
    prior = (sensitivity * prior) / (
        sensitivity * prior + false_positive * (1 - prior)
    )

print(prior)

#7
fraud_rate = 0.005
model_precision = 0.98

posterior = (model_precision * fraud_rate) / (
    model_precision * fraud_rate + (1 - model_precision) * (1 - fraud_rate)
)

print(posterior)

#8
excellent_rate = 0.05
good_interview_given_excellent = 0.9
good_interview_given_average = 0.3

posterior = (good_interview_given_excellent * excellent_rate) / (
    good_interview_given_excellent * excellent_rate +
    good_interview_given_average * (1 - excellent_rate)
)

print(posterior)

#9
fair_head = 0.5
biased_head = 0.9

posterior_biased = biased_head / (biased_head + fair_head)
print(posterior_biased)

#10
def should_treat(probability, threshold=0.7):
    return probability >= threshold

print(should_treat(0.65))

#11
prior = 0.1
evidence = [0.8, 0.7, 0.9]

for e in evidence:
    prior = (prior * e) / (prior * e + (1 - prior) * (1 - e))

print(prior)

#12
obstacle_rate = 0.001
sensor_accuracy = 0.99
false_alarm = 0.02

posterior = (sensor_accuracy * obstacle_rate) / (
    sensor_accuracy * obstacle_rate + false_alarm * (1 - obstacle_rate)
)

print(posterior)

#13
conversion_A = 0.04
conversion_B = 0.06

prob_B_better = conversion_B / (conversion_A + conversion_B)
print(prob_B_better)

#14
def classify(prior_yes, likelihood_yes, likelihood_no):
    return (prior_yes * likelihood_yes) / (
        prior_yes * likelihood_yes + (1 - prior_yes) * likelihood_no
    )

print(classify(0.3, 0.8, 0.2))

#15
prediction_confidence = 0.95
base_rate = 0.01

final_confidence = prediction_confidence * base_rate
print(final_confidence)




