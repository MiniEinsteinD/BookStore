-- by name
"SELECT b.name, b.ISBN FROM Book b WHERE b.name='" + searchname + "' AND EXISTS (SELECT 1 FROM Collection c WHERE c.owner='" + username + "' AND c.collection_name='" + collection + "' AND c.ISBN=b.ISBN)"

-- by genre 
"SELECT b.name b.ISBN FROM Book b WHERE EXISTS (SELECT 1 FROM Collection c WHERE c.owner='" + username + "' AND c.collection_name='" + collection + "' AND c.ISBN=b.ISBN) AND EXISTS (SELECT 1 FROM In_Genre g WHERE b.ISBN=g.ISBN AND g.genre='" + searchGenre + "')"

-- by author
"SELECT DISTINCT b.name b.ISBN FROM Book b WHERE EXISTS (SELECT 1 FROM Collection c WHERE c.owner='" + username + "' AND c.collection_name='" + collection + "' AND c.ISBN=b.ISBN) AND EXISTS (SELECT 1 FROM Is_Author a WHERE b.ISBN=a.ISBN AND a.first_name='" + searchfname + "' AND a.last_name='" + searchlname + "')"