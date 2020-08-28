## BUILDING A COMMUNITY APP: DIASPORA INDONESIA

### 0. Setup
### 1. Create project
### 2. Create src/home app and register it to project
### 3. Add static and media files, and create home/index.html template

	(venv38301) λ git status
	On branch master
	Changes to be committed:
	  (use "git reset HEAD <file>..." to unstage)

	        modified:   .gitignore
	        modified:   diaspora/settings.py
	        modified:   diaspora/urls.py
	        modified:   src/home/views.py
	        new file:   templates/home/index.html

### 4. Sagmenting index page

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

### 5. Tempate inheritance

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

### 6. Dynamic main home sliders & modified home template

    On branch master
    Your branch is up to date with 'origin/master'.

    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

            modified:   README.MD
            modified:   db.sqlite3
            modified:   src/home/__pycache__/admin.cpython-38.pyc
            modified:   src/home/__pycache__/models.cpython-38.pyc
            modified:   src/home/__pycache__/views.cpython-38.pyc
            modified:   src/home/admin.py
            new file:   src/home/migrations/0001_initial.py
            new file:   src/home/migrations/0002_auto_20200828_1658.py
            new file:   src/home/migrations/__pycache__/0001_initial.cpython-38.pyc
            new file:   src/home/migrations/__pycache__/0002_auto_20200828_1658.cpython-38.pyc
            modified:   src/home/models.py
            modified:   src/home/views.py
            modified:   templates/common/navbar.html
            modified:   templates/common/topbar.html
            deleted:    templates/home/component/ads.html
            modified:   templates/home/component/faq.html
            new file:   templates/home/component/perwakilan-ri.html
            modified:   templates/home/component/slider.html
            modified:   templates/home/index.html