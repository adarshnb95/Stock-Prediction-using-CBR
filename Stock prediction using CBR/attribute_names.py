## -*- coding: utf-8 -*-
##
## attribute_names.py
##
## Author:   Toke Høiland-Jørgensen (toke@toke.dk)
## Date:     26 April 2012
## Copyright (c) 2012, Toke Høiland-Jørgensen
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re

import attributes, tree

class SentimentScore(attributes.Numeric, attributes.ExactMatch):
    """JourneyCode attribute.

    Sentiment scores. Matches only if exact.

    Possible values: positive integers."""

    _weight = 100.0

#class HolidayType(attributes.TreeMatch):
    """HolidayType attribute.

    Different types of holiday. Similarity is based on a similarity
    tree for related types of holidays.

    Possible values: Active, Adventure, Arbitrary, Bathing, City,
    Diving, Education, Language, Recreation, Shopping, Skiing,
    Surfing, Wandering."""
"""
    _match_tree = tree.Tree(
        ["Arbitrary", 0.3, [
                ['Active', 0.5, [
                        ['Adventure', 1.0, []],
                        ['Diving', 1.0, []],
                        ['Skiing', 1.0, []],
                        ['Surfing', 1.0, []]]],
                ['City', 0.5, [
                        ['Shopping', 1.0, []]]],
                ['Education', 0.5,  [
                        ['Language', 1.0, []]]],
                ['Recreation', 0.6, [
                        ['Bathing', 1.0, []],
                        ['Wandering', 1.0, []]]]]])

    _weight = 10.0

    def _set_value(self, value):
        attributes.TreeMatch._set_value(self, value.capitalize())
"""
class StockPrice(attributes.LessIsPerfect, attributes.LinearAdjust):
    """Price of stock.

    Simple linear matching on price distance, with a less is perfect metric.

    When a case is adapted, this value is adjusted corresponding to
    the magnitude of adaptation of other parameters.

    Possible values: Positive integers."""
   
    _weight = 50.0


class CompanyType(attributes.TableMatch):
    """Type of Company.

    Possible values (considered so far): Technology, Medical, Entertainment, Manufacturing."""
    _match_table = {'Tech':   {'Apple': 1.0, 'Samsung': 0.8, 'Google': 0.0, 'IBM': 0.5},
                    'Medical': {'Cipla': 0.6, 'Johnson&Johnson': 1.0, 'Bell Labs': 0.0, 'Train': 0.8},
                    'Entertainment': {'Car': 0.0, 'Coach': 0.0, 'Plane': 1.0, 'Train': 0.3},
                    'Manufacturing': {'Car': 0.4, 'Coach': 0.8, 'Plane': 0.0, 'Train': 1.0},}

    _weight = 10.0

class StockPercentageChange(attributes.Float):

	_weight = 50.0
	
class NewsPosSentiment(attributes.Float):

	range = [0-100]
	_weight = 20.0
	
class NewsNegSentiment(attributes.Float):

	range = [0-100]
	_weight = 20.0
	
#class StockDifference(attributes.Float):

#	_weight = 30.0
	
class TwitterPosSentiment(attributes.Float): 
	range = [0-100]
	_weight = 10.0
	
class TwitterNegSentiment(attributes.Float): 
	range = [0-100]
	_weight = 10.0
	
#class Season(attributes.Attribute):
    """Holiday season.

    Time holiday takes place. Matching is done by matching holidays
    that are either in an adjacent month, or the same season (winter,
    spring...) half, and others not at all.

    Possible values: Month names (January...December)."""
"""
    # Month names
    _months = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
    # Seasons. Values are indexes in _months
    _seasons = [[11,0,1], # Winter
                [2,3,4],  # Spring
                [5,6,7],  # Summer
                [8,9,10]] # Autumn

    # Similarity for adjacent months / same season
    _fuzz_similarity = 0.5

    _weight = 2.0

    def _set_value(self, value):
        value_norm = value.capitalize()
        if not value_norm in self._months:
            raise ValueError("Unrecognised value for %s: '%s'." % (self.name, value))
        self._value = value_norm
"""
  #  def similarity(self, other):
        """Similarity metric for season. Perfect match if value is
        the same. Otherwise, _fuzz_similarity if it's an adjacent month
        or the same season"""
    """    if self.value == other.value:
            return self.weight

        idx_self = self._months.index(self.value)
        idx_other = self._months.index(other.value)
        season_self = 0
        season_other = 0
        for i,season in enumerate(self._seasons):
            if idx_self in season:
                season_self = i
            if idx_other in season:
                season_other = i

        # Return the "fuzz similarity" if the two values are in
        # the same season, or adjacent months. Wraparound on
        # months is not a problem in this case, since that occurs
        # within one season (winter)
        if season_self == season_other or abs(idx_self-idx_other) == 1:
            return self._fuzz_similarity*self.weight

        return 0.0
"""

