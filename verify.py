from playwright.sync_api import sync_playwright

def run_cuj(page):
    page.goto("http://localhost:4173") # Vite preview defaults to 4173
    page.wait_for_timeout(2000)

    # Click archery or just evaluate
    page.locator("#archery").focus()
    page.keyboard.press("Enter")
    page.wait_for_timeout(8000) # Wait for animation to mostly complete and branches to grow

    page.screenshot(path="/home/jules/verification/screenshots/verification2.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
