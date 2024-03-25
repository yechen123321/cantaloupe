# test1

## Project setup

```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Lints and fixes files

```
npm run lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

开发需求：

(1) 总发电功率：{
1. icon + 总发电量
2. icon + 风场数量
3. icon + 机组数量
4. icon + 可利用率
}
(2) 各区域风电发电功率：{
折线图
X：区域1, 2, 3 ...
Y：在单位时间内所产生的电功率，通常以瓦特（W）或千瓦（kW）为单位。 KW/h
}

(3) 各区域风电发电量：{
竖状条形图
Y：区域1, 2, 3 ...
X: KW
}

(4) 风电历史发电量：{
柔滑曲线图
X：1-12月份
Y：KW or More
}

(5) 风电装机比例饼图：{
各类型风力发电机装机容量比
name + number Show
}

(6) 各风机发电数据：{
发电转换率
日发电量
}

(7) 故障显示：{
name + thing
warning
call people deal
}

    