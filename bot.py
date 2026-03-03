from responses import questions, fallback_messages, final_fallback

class СhatBot:
    # Counter that tracks how many times the bot did not understand the user input
    def __init__(self):
        self.unknown_counter = 0

    # Returns a list of all available questions
    def get_questions(self):
        return [q["question"] for q in questions.values()]

    # Main function that receives user input and returns the bot's answer
    def get_answer(self, user_input):
        global unknown_counter

        user_input = user_input.lower().strip()

        for value in questions.values():
            if user_input == value["question"].lower():
                self.unknown_counter = 0
                return value["answer"]

        unknown_counter += 1

        # Return different fallback messages for the first few unknown questions
        if self.unknown_counter <= len(fallback_messages):
            return fallback_messages[self.unknown_counter - 1]

        return final_fallback