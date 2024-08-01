class Solution:
    def countSeniors(self, details):
        total_60plus_years = 0
        for info in details:
            phone_number = info[0:10]
            gender = info[10]
            age = int(info[11:13])
            seat = info[13:]
            if age > 60:
                total_60plus_years += 1

        return total_60plus_years