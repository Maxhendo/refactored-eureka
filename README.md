# the Universe
#### video Demo: https://www.youtube.com/watch?v=oZ6-59Rm_zQ
#### Description:
Project contains code for a rudimentary artifical narrow inteligence. Program prompt polar question in layman'e terms yes/no
quetion for input. The output is an appropriate amswer. The answers have various positive, negative, and neutral tones. To cover
a range of posibilties. The isplayed as a web link complete with optional login with secure hashing. Revealing About page explaining
thought process behind its creation. And allows for reviews to be entered by users.

Statis contains style.css and graphic used. Links Below:
[favicon](https://favicon.io/)
image used in top right.
[spacewallpaper.jpg](https://unsplash.com/wallpapers/nature/space)
image is the backdrop of website.

templates contains the 8 html files embodyng the website.

1. about is an alert triggering page that is a disclaimer to users curious about the develoment or intensions of the site.
2. index is the homepage made up of navigation bar, title, input prompt, and instructions.
3. layout is Head element details navbar instructions and footer.
4. login by entering username and password. Compared to information in magic database.
5. register by creating unique username. Double password confirmation hashed into magic database.
6. reveal displays answers to users' questions from index.
7. reviews display users testimony.
8. add provides a text area for user to give their opioion of the experinece.


## python
App assist contains login_required function to restrict access to review.html page.

application logic. Configuration of seesion to a temporay directory in filesystem instead of signed cookies.
Added is a SQlite database created Google spreed sheet and downloaded to a csv file. A list name linguistic
holds word used to idenitfy weather the question is a polar question. Next list is empty called testimony.
It will be filled as user leave reviews.

Following is route functions:

- home, display homepage. Navigationbar, Title, input, intructions.
- answer, Get method direct to homepage. Post generate a *random* number between 1 and 21. The number of
responces. The user's question is then *split* into a list of words. Boleen expression compares the first
word to the list of words in linguistics. If their is a match random number retrieves a responce using the
associated number. Then return response as an answer to reveal page. **OR** If their is no match the responce
retrieved is limited to a neutral condition. Propmting new input.
-about, on click direct to a information page.
-reviews, display reviews in database's testimony table.
-add, Get direct to add html. Post retrieves testimony from text area. Then *insert into* testimony table
with user_ID.
-reveal, Page displayed answer retrived from databases's responces table.
-login, session is cleared. Post confirm username is entered. Confirm password is entered. Then compare
inut to databases' users table. If the username and hash key match user is directed to homepage. Else error.
-logout, session is cleared then redirected to homepage.
-register, Post diect user to enter username and password else error. Password is converted a hash key. The
hash key and username is then entered into user table. Lastly redirected to login html.


## phpliteadmin
magic database contains three tables responces, users, reviewed. responces hold the answers randomly selected pending
question. users holds the login information. passwords are hashed for added secuirty. reviewed holds the comments listed
in reviews.

## txt
magic8ball- responces is a csv list of responces suited to answer polar questions. They are seperated by tone.

## Design choices
The orginally idea was an eight ball theme with the same purpose and logic. But the animation for a ball was outside my skill set.
I would have liked the ball to rotate and answer fade into a black circle. However HTML is limited to manipulaing
words. More boolen expression could have been added to attempt more accurate responces to predictable questions.
For example question containing "I" could automaticlly return a positive responce.

## Unsolved bugs
When the answer to the question in revealed in reveal.html, the answer appears with SQL label still showing.
It is an aesthtic issue.The same issue occurs when displaying testimony in reviews.html.
Content is not perferctly centered despite style code.
logic issues errors appear after registrtion. And redirect from add.html to reviews.html trigger errors.


