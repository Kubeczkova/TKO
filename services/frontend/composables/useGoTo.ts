import { useRouter, useRoute } from "vue-router";
import { nextTick } from "vue";

export async function useGoTo(
  selector: string,
  props: { offset?: number } = {}
): Promise<void> {
  const router = useRouter();
  const route = useRoute();
  const yOffset = props?.offset ?? -80;

  const hash = selector.startsWith("#") ? selector : "";
  const path = selector.startsWith("/") ? selector : route.path + hash;

  // If navigating to another page
  if (route.path !== path.split("#")[0]) {
    await router.push(path);
    await nextTick(); // Ensure DOM updates

    // Wait for the element to exist before scrolling
    try {
      const element = await waitForElement(hash);
      scrollToElement(element, yOffset);
    } catch (error) {
      console.warn(error);
    }
  } else {
    // If already on the correct page, scroll immediately
    try {
      const element = await waitForElement(hash);
      scrollToElement(element, yOffset);
    } catch (error) {
      console.warn(error);
    }
  }
}

// Scroll to the element smoothly
function scrollToElement(element: Element, offset: number) {
  const y = element.getBoundingClientRect().top + window.pageYOffset + offset;
  window.scrollTo({ top: y, behavior: "smooth" });
}

// Wait for the element to exist
function waitForElement(selector: string, timeout = 2000): Promise<Element> {
  return new Promise((resolve, reject) => {
    const startTime = Date.now();
    let observer: MutationObserver;

    function checkElement() {
      const element = document.querySelector(selector);
      if (element) {
        observer.disconnect(); // Stop observing DOM changes
        resolve(element);
      } else if (Date.now() - startTime >= timeout) {
        observer.disconnect(); // Stop observing DOM changes
        reject(new Error(`Timeout exceeded while waiting for element '${selector}'`));
      }
    }

    observer = new MutationObserver(checkElement);
    observer.observe(document.body, { childList: true, subtree: true });

    checkElement(); // Initial check in case the element already exists
  });
}
