# 테스트할 클래스

class AnonymousSurvey():
    """설문조사에서 익명 응답을 수집한다."""

    def __init__(self, question):
        """설문을 저장하고 응답을 저장할 준비를 한다."""

        self.question = question
        self.responses = []

    def show_question(self):
        """설문을 표시한다."""

        print(self.question)

    def store_response(self, new_response):
        """응답 하나를 저장한다."""
        self.responses.append(new_response)

    def show_results(self):
        """받은 응답을 모두 표시한다."""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
