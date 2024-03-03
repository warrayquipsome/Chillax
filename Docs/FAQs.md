<h1 align="center">C H I L L A X FAQs</h1>
<h3 align="center">Vencord Edition</h3>

### How to change the background/background image of CHILLAX?

The steps are first `settings`, then go to the `VENCORD` Section and then `Themes`.
Finally, click `Edit Quick CSS` which should open [Monaco](https://microsoft.github.io/monaco-editor/) code editor.
See the below-attached screenshots:

<img src="images/bg_change/go_to_settings.png" alt="whatever">
<img src="images/bg_change/edit_quick_css.png" alt="whatever">
<img src="images/bg_change/monaco_editor.png" alt="whatever">

Now to go to line number `46` (*at the time of writing the line number
is 46 which in a later version might change*) or where the variable `--wallpaper`
defined and change the url that is within the single quote `''`
to the wallpaper/gif **url** that you want to set.

See the below screenshots:

<img src="images/bg_change/bg_change.png" alt="whatever">

Now your favourite BG should be applied.

**Note**: If you are using discord CDN they expire after some time.
In such cases fetch a new link.

### How to change/use another font(s)?

First, make sure that the font you are trying to
use is already hosted somewhere if it's not already.
Most of the time you will be using [google fonts](https://fonts.google.com/).
From there, choose the font you are looking for and adjust all the settings
and everything (font weights, size etc.) and then copy the css import url.
See the below screenshots:

1. <img src="images/font_change/font_change_1.png" alt="wq is loading">
2. <img src="images/font_change/font_change_2.png" alt="wq is loading">
3. <img src="images/font_change/font_change_3.png" alt="wq is loading">
4. <img src="images/font_change/font_change_4.png" alt="wq is loading">
5. <img src="images/font_change/font_change_5.png" alt="wq is loading">
6. <img src="images/font_change/font_change_6.png" alt="wq is loading">

    * Only copy the highlighted part.
      In your case, the link maybe different.

7. <img src="images/font_change/font_change_7.png" alt="wq is loading">

    * Now go to `Settings` > `Themes` > `Edit Quick CSS`.
    * Paste the copied link at the top just like the above screenshot and put the `;` at the end of it.

8. <img src="images/font_change/font_change_8.png" alt="wq is loading">

    * Now change the `--font-nane` to the name of the font that you have
      just imported.
    * Optionally adjust the `--font-size` if you need to.

And Now the new fonts should be applied.

#### Alternatively, if you want to use a downloaded font:

* Host the font somewhere. [GitHub](https://www.github.com) is a good place.
* All you have to do it create a new repo and upload the font there.
* After click on the font file and get the **RAW** link of that.
* Now just like in the previous step 7, we import the font, but this time
  using the **RAW** GitHub link instead of Google font one.

```css
   @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap');
```

instead, it will be

```css
   @import url('RAW LINK'); /* Replace `RAW LINK` with the GitHub raw url/link */
```

### How to change the font size?

* Go to `Settings` > `Themes` > `Edit Quick CSS`.
* Find the css variable `--font-size` and change it to your needs.

That's it.

### How to change the accent color

* Go to `Settings` > `Themes` > `Edit Quick CSS`.
* Find the css variables `--accentcolor`, `--accentcolor2` and change them to your needs.
* You may want to play around with them to find the right balance.

**Note**: `--accentcolor` is for [rgb](https://imagecolorpicker.com/) and `--accentcolor2` is for [hex](https://imagecolorpicker.com/).

### How to change the theme welcome user name?

* Go to `Settings` > `Themes` > `Edit Quick CSS`.
* Find the css variables `--user-name` and change it.

### How to make it so that desktop `wallpaper/wallpaper engine's` wallpaper is visible through

**We recommend you to not go for that**


However, if you have decided to make up your mind then

* Go to `Settings` > `Vencord` > `Enable Window Transparency` and turn it on.
* Now `Settings` > `Themes` > `Edit Quick CSS` and remove `--wallpaper` css variable
  mentioned in [here](#how-to-change-the-backgroundbackground-image-of-chillax).
* Your window should now be `transparent` or `see through` etc.
* Now you may want to add a bit of blur to make things readable in the `container__037ed`.
  However, discord uses electron, and we have found it to work differently on different
  OS and window manager of your OS also plays a vital role here.
  So, the below css snippet may or may does not work properly (Translucence is enabled in
  window manager level).
  In case it does not work, it will at least make the window a bit darker.
  ```css
      .container__037ed {
            background-color: rgba(255, 255, 255, 0) !important; /* Semi-transparent white for light theme */
            /* Or use this for dark theme: background-color: rgba(0, 0, 0, 0.1); */
            backdrop-filter: blur(1px) !important; /*Blur the background*/
            border-radius: 10px; /* Rounded corners */
            /* Or use this for dark theme: border: 1px solid rgba(0, 0, 0, 0.2); */
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37) !important; /* Optional: Add a box shadow for depth */
      }
  ```
**Note**: *Linux users this may be a hit or miss due to infinite number of factors
  (Too many DEs, WMs & Display Protocols).* 
  But using WM you can **natively add/force** translucence
  at window level
  (i.e. [hyprland](https://hyprland.org/) [**wayland warning**], [qtile](https://qtile.org/), [KWin](https://userbase.kde.org/KWin) etc.), 
  and you won't have to do any of the above-mentioned things.