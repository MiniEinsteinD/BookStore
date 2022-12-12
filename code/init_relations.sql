#Insert user data
INSERT INTO Users VALUES ('user1', 'Ahmed', 'Elroby', '12345', '50');
INSERT INTO Users VALUES ('user2', 'Moe', 'Za', '54321', '500');
INSERT INTO Users VALUES ('user3', 'Dani', 'Mo', '12345D', '300');
INSERT INTO Owner VALUES ('owner1', 'Ali', 'Alex', '54321', '500');
INSERT INTO Owner VALUES ('owner2', 'Janet', 'Smith', '54321', '500');

#Insert publisher data
INSERT INTO Publisher VALUES ('publ1@test.ca', 'Bob', 'Ta', '54321t', '500');
INSERT INTO Publisher VALUES ('publ2@test.ca', 'John', 'Fa', '54321t', '450');
INSERT INTO Publisher VALUES ('publ3@test.ca', 'Tash', 'Feen', '54321t', '550');

#Insert book data
INSERT INTO Book VALUES ('1234567890001', 'book1', '482', '31', '0.85', 'publ1@test.ca');
INSERT INTO Book VALUES ('1234567890002', 'book2', '587', '22', '0.54', 'publ1@test.ca');
INSERT INTO Book VALUES ('1234567890003', 'book3', '399', '40', '0.63', 'publ1@test.ca');
INSERT INTO Book VALUES ('1234567890004', 'book4', '562', '33', '0.39', 'publ1@test.ca');
INSERT INTO Book VALUES ('1234567890005', 'book5', '453', '24', '0.74', 'publ1@test.ca');
INSERT INTO Book VALUES ('1234567890006', 'book6', '612', '27', '0.37', 'publ1@test.ca');
INSERT INTO Book VALUES ('1234567890007', 'book7', '382', '23', '0.82', 'publ1@test.ca');
INSERT INTO Book VALUES ('1234567890008', 'book8', '636', '35', '0.57', 'publ1@test.ca');
INSERT INTO Book VALUES ('1234567890009', 'book9', '443', '37', '0.46', 'publ1@test.ca');
INSERT INTO Book VALUES ('1234567890010', 'book10', '407', '29', '0.26', 'publ1@test.ca');
INSERT INTO Book VALUES ('1234567890011', 'book11', '622', '42', '0.76', 'publ2@test.ca');
INSERT INTO Book VALUES ('1234567890012', 'book12', '567', '42', '0.46', 'publ2@test.ca');
INSERT INTO Book VALUES ('1234567890013', 'book13', '287', '35', '0.78', 'publ2@test.ca');
INSERT INTO Book VALUES ('1234567890014', 'book14', '623', '41', '0.37', 'publ2@test.ca');
INSERT INTO Book VALUES ('1234567890015', 'book15', '349', '39', '0.19', 'publ2@test.ca');
INSERT INTO Book VALUES ('1234567890016', 'book16', '387', '46', '0.36', 'publ2@test.ca');
INSERT INTO Book VALUES ('1234567890017', 'book17', '408', '40', '0.27', 'publ2@test.ca');
INSERT INTO Book VALUES ('1234567890018', 'book18', '267', '27', '0.61', 'publ2@test.ca');
INSERT INTO Book VALUES ('1234567890019', 'book19', '452', '30', '0.37', 'publ2@test.ca');
INSERT INTO Book VALUES ('1234567890020', 'book20', '395', '40', '0.02', 'publ2@test.ca');
INSERT INTO Book VALUES ('1234567890021', 'book21', '518', '25', '0.28', 'publ3@test.ca');
INSERT INTO Book VALUES ('1234567890022', 'book22', '354', '38', '0.68', 'publ3@test.ca');
INSERT INTO Book VALUES ('1234567890023', 'book23', '638', '31', '0.51', 'publ3@test.ca');
INSERT INTO Book VALUES ('1234567890024', 'book24', '637', '48', '0.11', 'publ3@test.ca');
INSERT INTO Book VALUES ('1234567890025', 'book25', '511', '20', '0.65', 'publ3@test.ca');
INSERT INTO Book VALUES ('1234567890026', 'book26', '374', '48', '0.7', 'publ3@test.ca');
INSERT INTO Book VALUES ('1234567890027', 'book27', '607', '38', '0.39', 'publ3@test.ca');
INSERT INTO Book VALUES ('1234567890028', 'book28', '440', '36', '0.48', 'publ3@test.ca');
INSERT INTO Book VALUES ('1234567890029', 'book29', '521', '44', '0.19', 'publ3@test.ca');
INSERT INTO Book VALUES ('1234567890030', 'book30', '448', '47', '0.89', 'publ3@test.ca');

#Insert Address data
INSERT INTO Address VALUES ('K2OW0P', '1', 'street1', 'Ottawa', 'ON', 'Canada');
INSERT INTO Address VALUES ('K2OZ0P', '2', 'street2', 'Seattle', 'WN', 'USA');
INSERT INTO Address VALUES ('K2OZ0D', '3', 'street3', 'Bahagdad', 'BG', 'IQ');
INSERT INTO Address VALUES ('K2Y6Y5', '4', 'street4', 'Calgary', 'AL', 'Canada');

#Insert collection data
INSERT INTO Collection VALUES ('owner1', '1234567890001', 'collection1', '20');
INSERT INTO Collection VALUES ('owner1', '1234567890002', 'collection1', '3');
INSERT INTO Collection VALUES ('owner1', '1234567890003', 'collection1', '16');
INSERT INTO Collection VALUES ('owner1', '1234567890004', 'collection1', '3');
INSERT INTO Collection VALUES ('owner1', '1234567890005', 'collection1', '1');
INSERT INTO Collection VALUES ('owner1', '1234567890006', 'collection1', '13');
INSERT INTO Collection VALUES ('owner1', '1234567890007', 'collection1', '19');
INSERT INTO Collection VALUES ('owner1', '1234567890008', 'collection1', '1');
INSERT INTO Collection VALUES ('owner1', '1234567890009', 'collection1', '6');
INSERT INTO Collection VALUES ('owner1', '1234567890010', 'collection1', '9');
INSERT INTO Collection VALUES ('owner1', '1234567890011', 'collection1', '5');
INSERT INTO Collection VALUES ('owner1', '1234567890012', 'collection1', '16');
INSERT INTO Collection VALUES ('owner1', '1234567890013', 'collection1', '6');
INSERT INTO Collection VALUES ('owner1', '1234567890014', 'collection1', '18');
INSERT INTO Collection VALUES ('owner1', '1234567890015', 'collection1', '15');
INSERT INTO Collection VALUES ('owner1', '1234567890016', 'collection1', '1');
INSERT INTO Collection VALUES ('owner1', '1234567890017', 'collection1', '16');
INSERT INTO Collection VALUES ('owner1', '1234567890018', 'collection1', '1');
INSERT INTO Collection VALUES ('owner1', '1234567890019', 'collection1', '16');
INSERT INTO Collection VALUES ('owner1', '1234567890020', 'collection1', '16');
INSERT INTO Collection VALUES ('owner1', '1234567890021', 'collection1', '7');
INSERT INTO Collection VALUES ('owner1', '1234567890022', 'collection1', '13');
INSERT INTO Collection VALUES ('owner1', '1234567890023', 'collection1', '3');
INSERT INTO Collection VALUES ('owner1', '1234567890024', 'collection1', '9');
INSERT INTO Collection VALUES ('owner1', '1234567890025', 'collection1', '7');
INSERT INTO Collection VALUES ('owner1', '1234567890026', 'collection1', '18');
INSERT INTO Collection VALUES ('owner1', '1234567890027', 'collection1', '16');
INSERT INTO Collection VALUES ('owner1', '1234567890028', 'collection1', '16');
INSERT INTO Collection VALUES ('owner1', '1234567890029', 'collection1', '11');
INSERT INTO Collection VALUES ('owner1', '1234567890030', 'collection1', '15');
INSERT INTO Collection VALUES ('owner2', '1234567890001', 'collection2', '20');
INSERT INTO Collection VALUES ('owner2', '1234567890004', 'collection2', '14');
INSERT INTO Collection VALUES ('owner2', '1234567890007', 'collection2', '15');
INSERT INTO Collection VALUES ('owner2', '1234567890010', 'collection2', '10');
INSERT INTO Collection VALUES ('owner2', '1234567890013', 'collection2', '15');
INSERT INTO Collection VALUES ('owner2', '1234567890016', 'collection2', '6');
INSERT INTO Collection VALUES ('owner2', '1234567890019', 'collection2', '4');
INSERT INTO Collection VALUES ('owner2', '1234567890022', 'collection2', '1');
INSERT INTO Collection VALUES ('owner2', '1234567890025', 'collection2', '17');
INSERT INTO Collection VALUES ('owner2', '1234567890028', 'collection2', '14');
INSERT INTO Collection VALUES ('owner2', '1234567890003', 'collection3', '12');
INSERT INTO Collection VALUES ('owner2', '1234567890006', 'collection3', '6');
INSERT INTO Collection VALUES ('owner2', '1234567890009', 'collection3', '7');
INSERT INTO Collection VALUES ('owner2', '1234567890012', 'collection3', '12');
INSERT INTO Collection VALUES ('owner2', '1234567890015', 'collection3', '11');
INSERT INTO Collection VALUES ('owner2', '1234567890018', 'collection3', '2');
INSERT INTO Collection VALUES ('owner2', '1234567890021', 'collection3', '1');
INSERT INTO Collection VALUES ('owner2', '1234567890024', 'collection3', '11');
INSERT INTO Collection VALUES ('owner2', '1234567890027', 'collection3', '6');
INSERT INTO Collection VALUES ('owner2', '1234567890030', 'collection3', '2');

#Insert phone data
INSERT INTO Phone VALUES ('publ1@test.ca', '1234567890');
INSERT INTO Phone VALUES ('publ1@test.ca', '1234567891');
INSERT INTO Phone VALUES ('publ2@test.ca', '1234567892');
INSERT INTO Phone VALUES ('publ3@test.ca', '1234567893');

#Insert Is_Author data
INSERT INTO Is_Author VALUES ('1234567890001', 'authorf1', 'authorl1');
INSERT INTO Is_Author VALUES ('1234567890002', 'authorf2', 'authorl2');
INSERT INTO Is_Author VALUES ('1234567890003', 'authorf3', 'authorl3');
INSERT INTO Is_Author VALUES ('1234567890004', 'authorf4', 'authorl4');
INSERT INTO Is_Author VALUES ('1234567890005', 'authorf5', 'authorl5');
INSERT INTO Is_Author VALUES ('1234567890006', 'authorf6', 'authorl6');
INSERT INTO Is_Author VALUES ('1234567890007', 'authorf7', 'authorl7');
INSERT INTO Is_Author VALUES ('1234567890008', 'authorf8', 'authorl8');
INSERT INTO Is_Author VALUES ('1234567890009', 'authorf9', 'authorl9');
INSERT INTO Is_Author VALUES ('1234567890010', 'authorf10', 'authorl10');
INSERT INTO Is_Author VALUES ('1234567890011', 'authorf11', 'authorl11');
INSERT INTO Is_Author VALUES ('1234567890012', 'authorf12', 'authorl12');
INSERT INTO Is_Author VALUES ('1234567890013', 'authorf13', 'authorl13');
INSERT INTO Is_Author VALUES ('1234567890014', 'authorf14', 'authorl14');
INSERT INTO Is_Author VALUES ('1234567890015', 'authorf15', 'authorl15');
INSERT INTO Is_Author VALUES ('1234567890016', 'authorf16', 'authorl16');
INSERT INTO Is_Author VALUES ('1234567890017', 'authorf17', 'authorl17');
INSERT INTO Is_Author VALUES ('1234567890018', 'authorf18', 'authorl18');
INSERT INTO Is_Author VALUES ('1234567890019', 'authorf19', 'authorl19');
INSERT INTO Is_Author VALUES ('1234567890020', 'authorf20', 'authorl20');
INSERT INTO Is_Author VALUES ('1234567890021', 'authorf21', 'authorl21');
INSERT INTO Is_Author VALUES ('1234567890022', 'authorf22', 'authorl22');
INSERT INTO Is_Author VALUES ('1234567890023', 'authorf23', 'authorl23');
INSERT INTO Is_Author VALUES ('1234567890024', 'authorf24', 'authorl24');
INSERT INTO Is_Author VALUES ('1234567890025', 'authorf25', 'authorl25');
INSERT INTO Is_Author VALUES ('1234567890026', 'authorf26', 'authorl26');
INSERT INTO Is_Author VALUES ('1234567890027', 'authorf27', 'authorl27');
INSERT INTO Is_Author VALUES ('1234567890028', 'authorf28', 'authorl28');
INSERT INTO Is_Author VALUES ('1234567890029', 'authorf29', 'authorl29');
INSERT INTO Is_Author VALUES ('1234567890030', 'authorf30', 'authorl30');
INSERT INTO Is_Author VALUES ('1234567890001', 'authorf26', 'authorl26');
INSERT INTO Is_Author VALUES ('1234567890006', 'authorf1', 'authorl1');
INSERT INTO Is_Author VALUES ('1234567890002', 'authorf27', 'authorl27');
INSERT INTO Is_Author VALUES ('1234567890007', 'authorf2', 'authorl2');
INSERT INTO Is_Author VALUES ('1234567890003', 'authorf28', 'authorl28');
INSERT INTO Is_Author VALUES ('1234567890008', 'authorf3', 'authorl3');
INSERT INTO Is_Author VALUES ('1234567890004', 'authorf29', 'authorl29');
INSERT INTO Is_Author VALUES ('1234567890009', 'authorf4', 'authorl4');
INSERT INTO Is_Author VALUES ('1234567890005', 'authorf30', 'authorl30');
INSERT INTO Is_Author VALUES ('1234567890010', 'authorf5', 'authorl5');

#Insert In_Genre data
INSERT INTO In_Genre VALUES ('1234567890001', 'genre2');
INSERT INTO In_Genre VALUES ('1234567890002', 'genre3');
INSERT INTO In_Genre VALUES ('1234567890003', 'genre4');
INSERT INTO In_Genre VALUES ('1234567890004', 'genre5');
INSERT INTO In_Genre VALUES ('1234567890005', 'genre1');
INSERT INTO In_Genre VALUES ('1234567890005', 'genre6');
INSERT INTO In_Genre VALUES ('1234567890006', 'genre2');
INSERT INTO In_Genre VALUES ('1234567890007', 'genre3');
INSERT INTO In_Genre VALUES ('1234567890008', 'genre4');
INSERT INTO In_Genre VALUES ('1234567890009', 'genre5');
INSERT INTO In_Genre VALUES ('1234567890010', 'genre1');
INSERT INTO In_Genre VALUES ('1234567890010', 'genre6');
INSERT INTO In_Genre VALUES ('1234567890011', 'genre2');
INSERT INTO In_Genre VALUES ('1234567890012', 'genre3');
INSERT INTO In_Genre VALUES ('1234567890013', 'genre4');
INSERT INTO In_Genre VALUES ('1234567890014', 'genre5');
INSERT INTO In_Genre VALUES ('1234567890015', 'genre1');
INSERT INTO In_Genre VALUES ('1234567890015', 'genre6');
INSERT INTO In_Genre VALUES ('1234567890016', 'genre2');
INSERT INTO In_Genre VALUES ('1234567890017', 'genre3');
INSERT INTO In_Genre VALUES ('1234567890018', 'genre4');
INSERT INTO In_Genre VALUES ('1234567890019', 'genre5');
INSERT INTO In_Genre VALUES ('1234567890020', 'genre1');
INSERT INTO In_Genre VALUES ('1234567890020', 'genre6');
INSERT INTO In_Genre VALUES ('1234567890021', 'genre2');
INSERT INTO In_Genre VALUES ('1234567890022', 'genre3');
INSERT INTO In_Genre VALUES ('1234567890023', 'genre4');
INSERT INTO In_Genre VALUES ('1234567890024', 'genre5');
INSERT INTO In_Genre VALUES ('1234567890025', 'genre1');
INSERT INTO In_Genre VALUES ('1234567890025', 'genre6');
INSERT INTO In_Genre VALUES ('1234567890026', 'genre2');
INSERT INTO In_Genre VALUES ('1234567890027', 'genre3');
INSERT INTO In_Genre VALUES ('1234567890028', 'genre4');
INSERT INTO In_Genre VALUES ('1234567890029', 'genre5');
INSERT INTO In_Genre VALUES ('1234567890030', 'genre1');
INSERT INTO In_Genre VALUES ('1234567890030', 'genre6');

#Insert Lives_At data
INSERT INTO Lives_At VALUES ('user1', 'K2OW0P');
INSERT INTO Lives_At VALUES ('user2', 'K2OW0P');
INSERT INTO Lives_At VALUES ('user3', 'K2OZ0P');

#Insert Works_At data
INSERT INTO Works_At VALUES ('publ1@test.ca', 'K2OZ0D');
INSERT INTO Works_At VALUES ('publ2@test.ca', 'K2OZ0D');
INSERT INTO Works_At VALUES ('publ3@test.ca', 'K2Y6Y5');
