# Fluent Icons for Web

Based on Fluent UI System Icons - a collection of familiar, friendly and modern icons from Microsoft.

We customized it for developers to use on their websites

![fluent system icons](art/readme-banner.png)

## Icon List

[View the full list of regular icons](icons_regular.md)

## Use

### Installation
Include Fluent Icons in your project

Add a link to the /fonts/fluent-icons-for-web.css file into the <head> of each template or page where you want to use Fluent Icons.

<head>

```groovy
<head>
  <!--load all Fluent Icons styles -->
  <link href="/fonts/fluent-icons-for-web.css" rel="stylesheet">
</head>
```

### Add Icons to HTML

We designed Fluent Icons for use with inline elements, and we recommend that you stick with a consistent element in your project. We recommend using element with the Fluent Icons CSS classes for the style class for the style of icon you want to use and the icon name class with the prefix for the icon you want to use.

Here's an example:

<head>

```groovy
<!-- This example uses <i> element with: 
1. the `fiw` style class for style
2. the `align-center-horizontal-48-filled` icon with the `fiw-` prefix -->

<i class="fiw fiw-align-center-horizontal-48-filled"></i>
```

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct) or contact opencode@microsoft.com with any additional questions or comments.
