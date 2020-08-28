## BUILDING A COMMUNITY APP: DIASPORA INDONESIA

### 0. Setup
### 1. Create project
### 2. Create src folder to hold all of the apps
### 3. Create src/home app and register it to project
### 4. Add static and media files, and create home/index.html template

	(venv38301) λ git status
	On branch master
	Changes to be committed:
	  (use "git reset HEAD <file>..." to unstage)

	        modified:   .gitignore
	        modified:   diaspora/settings.py
	        modified:   diaspora/urls.py
	        modified:   src/home/views.py
	        new file:   templates/home/index.html

### 5. Sagmenting index page

	Changes to be committed:
  	(use "git reset HEAD <file>..." to unstage)

        modified:   README.MD
        new file:   templates/common/head.html
        new file:   templates/common/navbar.html
        new file:   templates/common/topbar.html
        new file:   templates/home/component/ads.html
        new file:   templates/home/component/faq.html
        new file:   templates/home/component/footer_active_members.html
        new file:   templates/home/component/footer_copyright.html
        new file:   templates/home/component/footer_widgets.html
        new file:   templates/home/component/how_it_works.html
        new file:   templates/home/component/most_popular_groups.html
        new file:   templates/home/component/most_popular_members.html
        new file:   templates/home/component/slider.html
        new file:   templates/home/component/sweet_moment.html
        modified:   templates/home/index.html

### 6. Tempate inheritance

    On branch master
    Your branch is ahead of 'origin/master' by 1 commit.
      (use "git push" to publish your local commits)

    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

            modified:   README.MD
            new file:   templates/base.html
            renamed:    templates/home/component/footer_active_members.html -> templates/common/footer_active_members.html
            renamed:    templates/home/component/footer_copyright.html -> templates/common/footer_copyright.html
            renamed:    templates/home/component/footer_widgets.html -> templates/common/footer_widgets.html
            modified:   templates/home/index.html