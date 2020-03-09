from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	#This is another test for git.
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_display_a_heroes_list_and_more_information_per_hero(self):
		# Widget has heard about a new wiki app for the game called The Will of the Wisps.
		# She goes to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention
		# 'The Will of the Wisps Wiki'
		self.assertIn('The Will of the Wisps Wiki', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('The Will of the Wisps Wiki', header_text)

		# She sees a list containing three heroes with their corresponding
		# names, health points, and damage
		hero_name_text = self.browser.find_elements_by_id('hero_name')
		self.assertIn('Cloud', hero_name_text)
		print(repr(hero_name_text))


		# When she selects one of the heroes, she is sent to another page
		# containing more information about the hero (additional stats, lore, image).

		# She spots the page title and header mentions the name of the hero she selected.

		# While she is in a specific hero's page, she sees a button labeled "Back to Heroes List".
		# She clicks this and she is redirected back to the wiki's homepage.

		self.fail('Finish the test!')

#main method
if __name__ == '__main__':
	unittest.main(warnings='ignore')
