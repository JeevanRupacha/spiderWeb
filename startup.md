
   <h3>Instruction for startup guide </h3>
        <h3>Github instruction </h3>
        <p>First you should create a project directory or folder where the project is going to be initialize .</p><br>
        <p>Start the git  command --> <strong>git init </strong> </p><br>
        <p>create your own branch  command --> <strong>git checkout -b "your branch name" </strong> <i> note: if your have already branch eliminate -b </i> </p> <br>
        <p> add repo inatialize command -> <strong> git remote add origin git@github.com:JeevanRupacha/spiderWeb.git < strong> or <strong> git remote add origin https://github.com/JeevanRupacha/spiderWeb.git </strong> </p> <br>
        <p>pull the repo -> command <strong> git pull git@github.com:JeevanRupacha/spiderWeb.git </strong> or <strong> git pull https://github.com/JeevanRupacha/spiderWeb.git</strong></p><br>
        <p> <i>Note : you can use git fetch origin or git clone link </i></p><br/>

        <h1>Well done !!😎😎</h1> 
        <p>Now you can work </p><br><br>

        <p> adding your file to version control command-> <strong>git add . <i> all file added</i> git add "filename" <strong></p><br>
        <p> saving the changes or committment the file  command-> <strong> git commit -m "your message" </strong></p> 

        <h3>After you finished project </h3>
        <h1>Merging Project </h1>
        <p> first push into github command-> <strong> git push origin "your branch name"<strong></p><br>
        <pre>
        step 1 : got to github repo
        step 2 : select your branch name by dropdown 
        step 3 : select pull request 
        step 4 : make sure to change with your co-worker or bosss
        step 5 : merge or rebase repo

        </pre>
        <p> Note : if there if merge conflicts conntact your co-workers </p><br><br>

        <h2> Useful git instructions </h2>
        <pre>
                git remote -v         --> for which repo you have been added
                git status            --> for all the status what changed 
                git log               --> for log of your commit 
                git branch            --> which branch current is
                git checkout master    --> switch the master branch 
                git merge "branch name" --> merge the current branch with name branch 
                git checkout -f         --> recover all the previous version file  i.e last commit 
                git diff                --> get changes 
                git rm filename          --> delete file 
                ssh-keygen               --> generate ssh key 
                cat "path ....rsa.pub"    --> get public ssh key
                ssh-T git@github.com      --> Access the ssh key 
                rm -rf .git     ----> delete all the git repo which was initialize
        </pre>
