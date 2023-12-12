SELECT firstName, lastName, city, state
FROM Person
LEFT JOIN Address ON Person.personID = Address.personID

-- we join the two tables on the personID column
-- regardless of whether there is a match in the Address table