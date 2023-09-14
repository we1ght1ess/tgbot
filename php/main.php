<!DOCTYPE html>
<html>
<head>
    <title>Регистрация</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
</head>
<style>
    body {
        background: #FDF4D9;
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        font-family: "Roboto", sans-serif;
        overflow: hidden;
    }
    div {
        font-family:Courier, monospace;
        font-size: 115%;
        width: 300px;
        text-align: center;
    }
    label{
        text-align: center;
    }
    input{
        text-align: center;
    }
</style>
<body>
<div class="container">
    <header class="d-flex justify-content-center py-3">
        <ul class="nav nav-pills">
            <li class="nav-item"><a href="#" class="nav-link active" aria-current="page">Регистрация</a></li>
            <li class="nav-item"><a href="#" class="nav-link">Вход</a></li>
            <li class="nav-item"><a href="#" class="nav-link">FAQs</a></li>
        </ul>
    </header>
</div>

<div class="container d-flex justify-content-center align-items-center" style="min-height: 50vh;">
    <?php if ($_SERVER['REQUEST_METHOD'] === 'GET') { ?>
    <form style="vertical-align: middle" action="main.php" method="post">
        <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label">Firstname</label>
            <input type="text" class="form-control" name="firstname" id="exampleFormControlInput1" value="<?php echo $_POST['firstname'] ?? '' ?>"placeholder="Имя">
        </div>

        <div class="mb-3">
            <label for="exampleFormControlInput2" class="form-label">Lastname</label>
            <input type="text" class="form-control" name="lastname" id="exampleFormControlInput2" value="<?php echo $_POST['lastname'] ?? '' ?>" placeholder="Фамилия">
        </div>

        <div class="mb-3">
            <label for="exampleFormControlInput3" class="form-label">Later</label>
            <input type="email" class="form-control" name="Later" id="exampleFormControlInput3" value="<?php echo $_POST['Later'] ?? '' ?>" placeholder="Почта">
        </div>

        <div class="mb-3">
            <label for="exampleFormControlInput4" class="form-label">Nickname</label>
            <input type="text" class="form-control" name="Nickname" id="exampleFormControlInput4" value="<?php echo $_POST['Nickname'] ?? '' ?>" placeholder="Никнейм">
        </div>

        <div class="mb-3">
            <label for="exampleFormControlInput4" class="form-label">Password</label>
            <input type="password" class="form-control" name="Пароль" id="exampleFormControlInput4" value="<?php echo $_POST['Nickname'] ?? '' ?>" placeholder="Придумайте пароль">
        </div>

        <div class="mb-3">
            <input type="submit" class="btn btn-primary" value="Сохранить">
        </div>
    </form>
    <?php
    }   
    ?>
</div>
<div class="container">
    <?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        echo '<b>firstname</b> = ' . ($_POST['firstname'] ?? '') . '<br>';
        echo 'lastname = ' . ($_POST['lastname'] ?? '');
        echo 'Later = ' . ($_POST['Later'] ?? '');
        echo 'Nickname = ' . ($_POST['Nickname'] ?? '');
        echo 'Пароль = ' . ($_POST['Пароль'] ?? '');
    }
    ?>
</div>


    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
</body>
</html>