#!/usr/bin/python3


class CheckPasswordPolicy:

    def solution1(self):

        counter = 0

        file = open('input.txt', 'r')

        for line in file:

            password_policy_details = line.split(' ')

            limits = password_policy_details[0].split('-')

            letter = password_policy_details[1].replace(':', '')

            char_count = password_policy_details[2].count(letter)

            if char_count >= int(limits[0]) and char_count <= int(limits[1]):

                counter += 1

        return counter

    def solution2(self):

        counter = 0

        file = open('input.txt', 'r')

        for line in file:

            password_policy_details = line.split(' ')

            limits = password_policy_details[0].split('-')

            letter = password_policy_details[1].replace(':', '')

            password = password_policy_details[2]

            if (password[int(limits[0])-1] == letter) and not (password[
                         int(limits[1])-1] == letter) or ((password[
                             int(limits[1])-1] == letter) and not (
                                 password[int(limits[0])-1] == letter)):

                counter += 1

        return counter


policy = CheckPasswordPolicy()

print(policy.solution1())
print(policy.solution2())

