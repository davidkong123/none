"""
    population = [
        [5, 324, 241, 98, 77, 119, 244, 217, 69, 20, 166, 85, 176, 228, 148],
        [5, 319, 252, 119, 22, 113, 274, 216, 46, 20, 166, 53, 167, 182, 170],
        [5, 319, 252, 92, 75, 119, 241, 227, 53, 20, 166, 49, 167, 191, 166],
        [5, 319, 252, 119, 75, 113, 267, 214, 60, -14, 161, 79, 167, 217, 146],
        [5, 319, 252, 119, 30, 113, 260, 192, 69, 20, 185, 70, 176, 217, 146],
        [5, 326, 252, 119, 17, 113, 258, 216, 53, 20, 189, 79, 167, 245, 146],
        [5, 319, 252, 63, 73, 113, 267, 214, 60, -14, 161, 79, 167, 217, 161],
        [5, 314, 252, 117, 75, 113, 244, 210, 67, 34, 189, 79, 167, 245, 146],
        [5, 319, 252, 121, 75, 119, 250, 196, 57, -14, 166, 94, 169, 227, 153],
        [5, 319, 252, 119, 30, 113, 260, 192, 61, 20, 166, 48, 167, 182, 170],
        [5, 319, 276, 79, 72, 113, 266, 210, 86, 20, 138, 91, 167, 217, 146],
        [5, 319, 276, 79, 72, 113, 260, 210, 67, 20, 189, 64, 185, 241, 164],
        [5, 296, 295, 79, 75, 123, 230, 210, 67, 20, 166, 85, 176, 217, 146],
        [5, 309, 276, 79, 75, 113, 260, 216, 57, 20, 166, 48, 167, 182, 170],
        [5, 319, 276, 79, 75, 113, 230, 210, 67, 20, 166, 85, 185, 217, 148],
        [5, 311, 290, 72, 75, 113, 230, 206, 67, 20, 161, 79, 167, 228, 146],
        [5, 319, 266, 81, 73, 113, 260, 210, 67, 20, 166, 66, 176, 228, 148],
        [5, 319, 252, 119, 30, 113, 260, 192, 69, 20, 166, 81, 185, 245, 146],
        [5, 319, 252, 119, 57, 113, 260, 210, 67, 20, 151, 81, 167, 231, 146],
        [5, 317, 266, 81, 73, 113, 267, 214, 60, -14, 161, 96, 167, 217, 148],
        [5, 319, 252, 119, 72, 113, 260, 210, 67, 20, 166, 94, 170, 228, 148],
        [5, 319, 276, 79, 72, 113, 253, 210, 67, 20, 138, 79, 167, 217, 146],
        [5, 304, 252, 119, 75, 113, 260, 216, 57, 20, 166, 85, 208, 217, 148],
        [5, 319, 266, 81, 73, 113, 267, 214, 60, -14, 161, 49, 167, 191, 170],
        [5, 319, 295, 119, 30, 113, 269, 192, 53, 34, 189, 79, 167, 245, 146],
        [5, 319, 266, 79, 57, 113, 230, 210, 67, 20, 151, 81, 167, 245, 146],
        [5, 325, 276, 79, 85, 113, 267, 214, 60, -14, 153, 79, 167, 217, 146],
        [5, 319, 252, 119, 30, 113, 260, 192, 69, 9, 158, 49, 167, 182, 170],
        [5, 319, 276, 79, 75, 113, 244, 210, 53, 20, 188, 79, 167, 232, 148],
        [5, 324, 295, 119, 30, 113, 260, 192, 69, 20, 166, 48, 167, 182, 170],
        [5, 319, 266, 81, 73, 113, 260, 216, 57, 20, 166, 85, 185, 217, 148],
        [5, 308, 236, 98, 75, 119, 244, 229, 67, -14, 166, 94, 169, 227, 153],
        [5, 319, 276, 79, 72, 113, 230, 210, 67, 20, 151, 81, 185, 245, 146],
        [5, 319, 252, 119, 72, 113, 260, 210, 67, 20, 166, 79, 167, 217, 150],
        [5, 319, 276, 65, 72, 113, 266, 210, 86, 20, 166, 79, 167, 245, 146],
        [5, 319, 252, 119, 73, 113, 267, 214, 60, -14, 161, 79, 167, 217, 146],
        [5, 319, 266, 81, 73, 119, 261, 214, 60, -14, 161, 79, 167, 217, 146],
        [5, 319, 252, 119, 22, 113, 268, 216, 57, 20, 166, 53, 167, 182, 170],
        [5, 319, 266, 81, 73, 113, 267, 214, 60, -14, 161, 79, 167, 217, 143],
        [5, 308, 252, 98, 75, 119, 261, 196, 53, 20, 168, 64, 167, 245, 156],
        [5, 319, 252, 119, 30, 113, 253, 210, 67, 20, 127, 91, 167, 217, 170],
        [5, 319, 266, 117, 75, 113, 230, 210, 67, 20, 151, 81, 185, 245, 146],
        [5, 319, 266, 81, 73, 113, 260, 216, 57, 20, 166, 85, 185, 217, 148],
        [5, 319, 252, 119, 30, 113, 260, 210, 67, 20, 158, 96, 167, 245, 146],
        [5, 319, 252, 119, 30, 113, 260, 192, 60, -14, 161, 79, 167, 217, 146],
        [5, 314, 252, 79, 72, 113, 260, 210, 67, 20, 166, 79, 167, 217, 146],
        [5, 303, 255, 119, 30, 113, 263, 192, 69, 3, 166, 57, 167, 189, 170],
        [5, 316, 276, 79, 88, 99, 260, 210, 67, 1, 141, 81, 167, 261, 146],
        [5, 319, 252, 119, 75, 120, 260, 216, 57, 20, 166, 85, 185, 217, 148],
        [5, 319, 252, 119, 30, 113, 274, 210, 67, -12, 166, 79, 167, 217, 146],
        [5, 319, 266, 81, 73, 113, 267, 214, 60, -14, 161, 79, 167, 182, 170],
        [5, 319, 266, 81, 73, 113, 267, 214, 60, -14, 161, 79, 167, 217, 146],
        [5, 319, 252, 119, 30, 113, 278, 192, 71, 20, 151, 81, 190, 245, 146],
        [5, 319, 252, 117, 75, 113, 230, 210, 67, 20, 151, 81, 185, 245, 146],
        [5, 319, 295, 138, 75, 113, 260, 210, 67, 20, 158, 96, 167, 182, 170],
        [5, 319, 252, 119, 19, 113, 260, 192, 69, 20, 185, 85, 162, 245, 146],
        [5, 319, 276, 79, 75, 113, 230, 210, 67, 20, 151, 48, 167, 182, 148],
        [5, 296, 276, 79, 72, 113, 244, 210, 67, 20, 138, 91, 167, 210, 146],
        [5, 308, 252, 94, 75, 119, 261, 196, 53, 20, 168, 64, 167, 245, 146],
        [5, 319, 295, 119, 30, 113, 260, 192, 69, 20, 166, 85, 176, 228, 148],
        [5, 319, 276, 98, 75, 119, 261, 196, 53, 20, 168, 64, 167, 245, 156],
        [5, 319, 276, 79, 75, 113, 260, 216, 57, 20, 166, 74, 185, 241, 164],
        [5, 308, 266, 81, 73, 113, 267, 214, 60, -14, 161, 67, 167, 217, 146],
        [5, 319, 252, 119, 30, 113, 268, 216, 57, 20, 166, 53, 167, 182, 170],
        [5, 319, 295, 98, 75, 119, 251, 229, 67, 20, 166, 85, 176, 228, 148],
        [5, 314, 252, 117, 75, 113, 230, 210, 67, 20, 151, 81, 185, 245, 146],
        [5, 319, 276, 79, 72, 99, 260, 210, 67, 1, 151, 81, 167, 228, 148],
        [5, 319, 295, 98, 75, 119, 244, 210, 67, 1, 151, 81, 167, 245, 146],
        [5, 319, 276, 117, 78, 113, 260, 216, 57, 20, 166, 79, 167, 245, 146],
        [5, 319, 252, 119, 30, 113, 260, 192, 69, 20, 166, 48, 167, 182, 170],
        [5, 319, 252, 99, 22, 113, 268, 216, 57, 20, 166, 53, 167, 182, 170],
        [5, 314, 252, 117, 75, 113, 230, 210, 67, 20, 166, 85, 176, 246, 148],
        [5, 317, 266, 81, 73, 113, 267, 214, 60, -14, 161, 79, 167, 217, 164],
        [5, 319, 276, 79, 72, 113, 260, 199, 67, 20, 189, 79, 167, 217, 146],
        [5, 319, 252, 119, 35, 113, 260, 192, 69, 20, 166, 48, 167, 228, 148],
        [5, 319, 252, 119, 30, 113, 260, 210, 67, 20, 189, 79, 179, 245, 156],
        [5, 319, 295, 98, 75, 119, 244, 229, 67, -14, 166, 94, 169, 227, 170],
        [5, 319, 276, 98, 75, 119, 261, 196, 53, 9, 158, 49, 167, 182, 170],
        [5, 319, 252, 98, 75, 119, 244, 229, 67, -14, 166, 94, 169, 227, 153],
        [5, 314, 252, 117, 75, 113, 230, 210, 67, 20, 166, 48, 167, 182, 170],
        [5, 314, 252, 117, 75, 113, 230, 210, 67, 26, 151, 81, 185, 245, 146],
        [5, 319, 276, 117, 75, 113, 230, 210, 67, 20, 151, 81, 185, 245, 146],
        [5, 319, 252, 119, 30, 113, 260, 192, 69, 20, 166, 48, 167, 245, 146],
        [5, 319, 276, 79, 75, 113, 244, 210, 62, 20, 201, 77, 167, 217, 148],
        [5, 314, 252, 92, 58, 119, 244, 217, 80, -14, 182, 94, 169, 227, 143],
        [5, 324, 241, 98, 77, 113, 274, 210, 67, -12, 166, 94, 167, 245, 146],
        [5, 319, 276, 79, 75, 113, 230, 210, 67, 20, 151, 48, 167, 245, 146],
        [5, 319, 257, 79, 75, 113, 230, 210, 67, 20, 151, 81, 167, 228, 170],
        [5, 296, 276, 79, 72, 99, 261, 196, 53, 10, 168, 80, 167, 245, 141],
        [5, 324, 241, 81, 73, 113, 267, 214, 60, -14, 161, 79, 167, 217, 146],
        [5, 308, 252, 98, 75, 119, 261, 196, 53, 20, 168, 64, 171, 245, 156],
        [5, 319, 276, 117, 78, 113, 260, 192, 69, 20, 166, 48, 167, 228, 148],
        [5, 296, 295, 79, 75, 113, 230, 210, 67, 20, 166, 85, 185, 217, 148],
        [5, 319, 276, 59, 72, 113, 260, 210, 67, 20, 166, 85, 185, 217, 148],
        [5, 314, 252, 117, 75, 113, 230, 210, 67, 20, 151, 81, 167, 182, 170],
        [5, 336, 295, 98, 75, 119, 244, 210, 67, 20, 166, 79, 182, 217, 156],
        [5, 314, 252, 92, 75, 119, 250, 196, 67, 20, 166, 96, 185, 217, 148],
        [5, 319, 276, 79, 72, 113, 260, 210, 67, 20, 189, 70, 185, 245, 159],
        [5, 296, 276, 79, 72, 99, 250, 196, 59, 47, 152, 79, 167, 185, 165],
        [5, 319, 276, 79, 72, 113, 260, 210, 67, 20, 189, 79, 167, 182, 170]]


    def get_points(self, board, player):
        return [self.most_vertical(board, player),
                self.most_horizontal(board, player),
                self.most_inc_diagonal(board, player),
                self.most_dec_diagonal(board, player)]


    def eval_board(self, board, depth=0):

        Computes a score for the given board state
        This method collects data from the board then multiplies them
        by corresponding values found in the dna array.

        points = self.get_points(board, self.ai)
        enemy_points = self.get_points(board, self.human)
        if 4 in enemy_points:
            return -math.inf + depth * 20
        elif 4 in points:
            return math.inf - depth * 20
        score = (sum(points) * 324 +
                 points.count(3) * 241 +
                 points.count(2) * 98 +
                 points[0] * 77 +
                 points[1] * 119 +
                 points[2] * 244 +
                 points[3] * 217)
        enemy_score = (sum(enemy_points) * 69 +
                       enemy_points.count(3) * 20 +
                       enemy_points.count(2) * 166 +
                       enemy_points[0] * 85 +
                       enemy_points[1] * 176 +
                       enemy_points[2] * 228 +
                       enemy_points[3] * 148)
        return score - enemy_score
    """
#from selenium import webdriver
import time


#browser = webdriver.Chrome('E:/4inarow/chromedriver.exe')
#browser.get("https://connect4.gamesolver.org/")
#time.sleep(5)
#temp = browser.find_element_by_id()
#temp.click()
