##工作区和暂存区和版本库

#Basic knowledge
工作区，就是我们能看到的文件夹。

版本库，存在于工作区隐藏目录.git下。

暂存区(stage)，是版本库中一个最重要的部分。

#Basic oprtion

## Add 
git add 实际上是把文件修改添加到暂存区。

git commit 实际上是把暂存区所有内容提交到当前分支。

简单理解：需要提交的文件修改通通先放到暂存区，然后，一次性提交暂存区的所有修改到当前分支。

#Assistance
git diff会拿工作区的文件和版本库或者暂存区的修改对比。如果用git add添加了文件,那么工作区的文件版本就和暂存区的文件版本一样，git diff就不会显示了。

##Revert
git checkout -- \<file\> 可以丢弃工作区修改，将工作区文件状态会退到上一次add或commit时。

git reflog 可以查看git操作记录，里边有版本号。

git reset --hard HEAD^|id 将项目回退到上一个版本，或会退到id指示的版本。

##Use Github
git remote add \<remotename\> git@github.com:\<account\>/\<reponame\>

git push -u \<remotename\> master

