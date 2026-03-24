# Canvas Homework Manager

This mango submodule facilitates automatic discovery, downloading, preambling and submission of homework distributed on canvas.

## Commands

- `mango list`
	- List available homeworks online.
	- Ordered by due time (`due_at`).
	- Status prefix `[downloaded|submitted]`, where each value is `Y` or `N`.

- `mango fetch <assignment-id|name-keyword>`
	- Fetch one homework from Canvas.
	- Downloads linked files from the assignment page.
	- Creates local structure under `homework/<id>-<slug>/`.
	- Executes `post_fetch_homework()` hook in `.mango/settings.py`.

- `mango submit <assignment-id|name-keyword>`
	- Runs `build_homework()` hook in `.mango/settings.py`.
	- Collects artifacts from `get_submission_artifacts()`.
	- Uploads files and submits them to Canvas.

## Configuration surface

Edit [.mango/settings.py](.mango/settings.py) to customize:

- Course/API settings (`OC_BASE_URL`, `OC_COURSE_ID`, `OC_API_KEY`, etc.)
- Which assignments count as homeworks (`choose_homework_assignments()`)
- How query strings match homeworks (`match_homework_query()`)
- How file links are parsed (`extract_homework_file_api_endpoints()`)
- Post-fetch setup behavior (`post_fetch_homework()`)
- Build + submission artifact logic (`build_homework()`, `get_submission_artifacts()`)