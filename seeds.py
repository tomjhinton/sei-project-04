from pony.orm import db_session
from app import db
from models.Ad import Ad
from models.Medium import Medium
from models.Work import Work
from models.User import User, UserSchema
from datetime import datetime, timedelta

db.drop_all_tables(with_all_data=True)
db.create_tables()

with db_session():



    schema = UserSchema()
    animation = Medium(name='Animation')
    music = Medium(name='Music')
    application = Medium(name='Application')
    illustration = Medium(name='Illustration')


    Hiro = User(
    username='Hiro Protagonist',
    email='Tomjhinton@gmail.com',
    password_hash=schema.generate_hash('pass'),
    lookingforwork=True,
	photo="https://66.media.tumblr.com/73d02ec8972950c826286b1b131c52cd/tumblr_oxtpvh44kI1w3debko1_1280.png"
    ,
    bio="""Hiro Protganoist creates media artworks and mixed media artworks. By parodying mass media by exaggerating certain formal aspects inherent to our contemporary society, Protganoist makes works that can be seen as self-portraits. Sometimes they appear idiosyncratic and quirky, at other times, they seem typical by-products of American superabundance and marketing.

    His media artworks often refers to pop and mass culture. Using written and drawn symbols, a world where light-heartedness rules and where rules are undermined is created. By manipulating the viewer to create confusion, he touches various overlapping themes and strategies. Several reoccurring subject matter can be recognised, such as the relation with popular culture and media, working with repetition, provocation and the investigation of the process of expectations.

    His works are saturated with obviousness, mental inertia, clichés and bad jokes. They question the coerciveness that is derived from the more profound meaning and the superficial aesthetic appearance of an image. By using popular themes such as sexuality, family structure and violence, he often creates several practically identical works, upon which thoughts that have apparently just been developed are manifested: notes are made and then crossed out again, ‘mistakes’ are repeated.

    His works are on the one hand touchingly beautiful, on the other hand painfully attractive. Again and again, the artist leaves us orphaned with a mix of conflicting feelings and thoughts.""")

    Molly = User(
    username='Molly Millions',
    email='Molly@gmail.com',
    password_hash=schema.generate_hash('pass'),
    lookingforwork=True,
	photo="http://i.imgur.com/oU6Vc.jpg"
    ,
    bio="""Molly Millions creates mixed media artworks, installations and conceptual artworks. By using an ever-growing archive of found documents to create autonomous artworks, Millions reflects on the closely related subjects of archive and memory. This often results in an examination of both the human need for ‘conclusive’ stories and the question whether anecdotes ‘fictionalise’ history.

    Her mixed media artworks demonstrate how life extends beyond its own subjective limits and often tells a story about the effects of global cultural interaction over the latter half of the twentieth century. It challenges the binaries we continually reconstruct between Self and Other, between our own ‘cannibal’ and ‘civilized’ selves. By demonstrating the omnipresent lingering of a ‘corporate world’, she makes work that generates diverse meanings. Associations and meanings collide. Space becomes time and language becomes image.

    Her works are an investigation of concepts such as authenticity and objectivity by using an encyclopaedic approach and quasi-scientific precision and by referencing documentaries, ‘fact-fiction’ and popular scientific equivalents. By studying sign processes, signification and communication, her works references post-colonial theory as well as the avant-garde or the post-modern and the left-wing democratic movement as a form of resistance against the logic of the capitalist market system.

    Her works question the conditions of appearance of an image in the context of contemporary visual culture in which images, representations and ideas normally function. Molly Millions currently lives and works in Chiba.""")

    Johnny = User(
    username='Johnny Mnemonic',
    email='Johnny@gmail.com',
    password_hash=schema.generate_hash('pass'),
    lookingforwork=True,
	photo="tom.png"
    ,
    bio = """Johnny Mnemonic is an artist who works in a variety of media. By emphasising aesthetics, Mnemonic seduces the viewer into a world of ongoing equilibrium and the interval that articulates the stream of daily events. Moments are depicted that only exist to punctuate the human drama in order to clarify our existence and to find poetic meaning in everyday life.

    His artworks are given improper functions: significations are inversed and form and content merge. Shapes are dissociated from their original meaning, by which the system in which they normally function is exposed. Initially unambiguous meanings are shattered and disseminate endlessly. In a search for new methods to ‘read the city’, he tries to create works in which the actual event still has to take place or just has ended: moments evocative of atmosphere and suspense that are not part of a narrative thread. The drama unfolds elsewhere while the build-up of tension is frozen to become the memory of an event that will never take place.

    His works sometimes radiate a cold and latent violence. At times, disconcerting beauty emerges. The inherent visual seductiveness, along with the conciseness of the exhibitions, further complicates the reception of their manifold layers of meaning. By putting the viewer on the wrong track, he focuses on the idea of ‘public space’ and more specifically on spaces where anyone can do anything at any given moment: the non-private space, the non-privately owned space, space that is economically uninteresting.

    His works are often about contact with architecture and basic living elements. Energy (heat, light, water), space and landscape are examined in less obvious ways and sometimes developed in absurd ways. Johnny Mnemonic currently lives and works in Bejing.""")

    company = User(
    username='Tyrell Corporation',
    email='Company@gmail.com',
    password_hash=schema.generate_hash('pass'),
    lookingforwork=True,
    medium=animation,
	photo="https://i.ytimg.com/vi/QgHXba9TgG0/maxresdefault.jpg"
    )

    lildata = User(
    username='Lil Data',
    email='data@gmail.com',
    password_hash=schema.generate_hash('pass'),
    lookingforwork=True,
    medium=music,
	photo="https://media.ntslive.co.uk/crop/769x769/383b629a-0a34-431a-a4a4-46c26e5ea5f7_1510704000.png",
    bio="""I tgohteer with my friends were actually examining the good points from your web page and then the sudden developed an awful suspicion I had not thanked the web blog owner for them. My boys came as a result passionate to see them and have in effect truly been making the most of them. I appreciate you for really being simply accommodating and for settling on this sort of ideal areas most people are really desirous to learn about. OUR own sincere apologies for not expressing gratitude to sooner. \n\n

    But the cry “We can do it” before we could, “We are doing it” before we did it, was too loud, too distinct, too often repeated, partly by men whose testimony had a real value in itself, and deserved attention. But it had too much charm for us; we made more of it than it really said or meant. Briefly, the time as it was, dazzled us; yet we still worked actively, in order practically to approach our end. We succeeded in many respects in the way of bringing a few beginning subjects of instruction into better order and to a better psychological foundation; and our efforts on this side might have had really important results; but the practical activity, which alone could secure the success of our purpose, was gradually lost in our midst in a lamentable manner. Matters strange and far removed from our duty soon absorbed our time and powers, and gave a mortal blow to the simplicity, the progress, the concentration, and even the humanity of our original efforts. Great ideas for improving the world, which arose out of elevated views of our subject, and which soon became exaggerated, filled our heads, confused our hearts, and made our hands careless of the needs that lay before our eyes."""
    )


    cyberdyne = User(
    username='Cyberdyne Systems',
    email='Company2@gmail.com',
    password_hash=schema.generate_hash('pass'),
    lookingforwork=True,
    medium=animation,
	photo="https://cdn.shopify.com/s/files/1/1158/9490/products/C000017974-PAR-ZOOM_b559d54f-6c74-4cee-9026-f6086148f294_800x.jpg?v=1527298174"
    )


    Work(
        createdBy=Hiro,
        created="2018/07/02",
        name="Python pic 1",
        picture="https://66.media.tumblr.com/2e27aafca3635fc39ed986936b50379e/tumblr_ps9jc4j0UH1w3debko1_1280.png",
        description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tristique neque ut accumsan tristique. Cras leo felis, semper in eleifend placerat, efficitur a nunc. Morbi fringilla egestas ante, vitae lacinia nunc vestibulum vitae. Mauris auctor dui eget gravida viverra. Pellentesque vel ultricies diam, sit amet dapibus leo. Morbi mattis enim elit, a imperdiet augue tempor ut. Suspendisse suscipit eleifend dui, bibendum consectetur arcu tristique vel. Nam nec risus aliquet, porttitor quam nec, ultrices sapien. Etiam in iaculis enim. Morbi ultricies semper arcu, vel luctus nulla iaculis auctor. Praesent vitae augue vitae lectus ultrices venenatis sit amet non dolor. Fusce dapibus dignissim nulla sit amet lacinia. Fusce non tortor ac quam vestibulum viverra. Praesent a lectus et dolor consequat aliquet vitae non turpis. Nullam et nulla vitae mi ultrices viverra. Integer sodales arcu velit, a faucibus neque dapibus ut.\n\n

        Curabitur tempus risus sit amet mi finibus mattis. Quisque gravida tempor tortor at consequat. Duis vulputate interdum leo id congue. Maecenas rhoncus nec ligula ut malesuada. Pellentesque volutpat felis ligula, vitae dapibus augue faucibus a. Aenean sagittis enim at quam accumsan, a varius lectus dignissim. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Ut imperdiet arcu ipsum, et porttitor velit scelerisque ut. Vivamus vitae semper mi, eu efficitur neque.""",
        medium=illustration,
        code="""from PIL import Image, ImageDraw, ImageFilter


        #im = Image.open("6MzjjikJ_400x400.jpg")
        im = Image.open("29.png")

        im1 = im.filter(ImageFilter.CONTOUR)
        im1 = im.filter(ImageFilter.FIND_EDGES)
        im6 = im1.filter(ImageFilter.BLUR)
        im5 = im6.filter(ImageFilter.CONTOUR)
        im7 = im5.filter(ImageFilter.EDGE_ENHANCE)
        im8 = im7.filter(ImageFilter.EDGE_ENHANCE)
        im2 = im.filter(ImageFilter.MinFilter(3))
        im3 = im.filter(ImageFilter.MinFilter)  # same as MinFilter(3)
        im8.save('29.png')
        """
        )

    Work(
            createdBy=lildata,
            created="2018/09/02",
            name="Live at London Algorave for TOPLAP15",
            picture="https://i.ytimg.com/vi/yOam-0c0og4/hqdefault.jpg",
            description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam tristique neque ut accumsan tristique. Cras leo felis, semper in eleifend placerat, efficitur a nunc. Morbi fringilla egestas ante, vitae lacinia nunc vestibulum vitae. Mauris auctor dui eget gravida viverra. Pellentesque vel ultricies diam, sit amet dapibus leo. Morbi mattis enim elit, a imperdiet augue tempor ut. Suspendisse suscipit eleifend dui, bibendum consectetur arcu tristique vel. Nam nec risus aliquet, porttitor quam nec, ultrices sapien. Etiam in iaculis enim. Morbi ultricies semper arcu, vel luctus nulla iaculis auctor. Praesent vitae augue vitae lectus ultrices venenatis sit amet non dolor. Fusce dapibus dignissim nulla sit amet lacinia. Fusce non tortor ac quam vestibulum viverra. Praesent a lectus et dolor consequat aliquet vitae non turpis. Nullam et nulla vitae mi ultrices viverra. Integer sodales arcu velit, a faucibus neque dapibus ut.\n\n

            Curabitur tempus risus sit amet mi finibus mattis. Quisque gravida tempor tortor at consequat. Duis vulputate interdum leo id congue. Maecenas rhoncus nec ligula ut malesuada. Pellentesque volutpat felis ligula, vitae dapibus augue faucibus a. Aenean sagittis enim at quam accumsan, a varius lectus dignissim. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Ut imperdiet arcu ipsum, et porttitor velit scelerisque ut. Vivamus vitae semper mi, eu efficitur neque.""",
            medium=music,
            code="""do -- zpbb3
                  bps (127/120)
                  d1 . m . sl 2 -- zp 1
                     . ev 4 (# hpf' "1e3 4e3 7e3" 0.3)
                     $ struct "t(3,8)!2" $ n ("0 1") # s "cutzpbb3"
                     + sp "1 [1 0.5? 0.25?]" # rvb "0.1:0.1"
                     # gco "0.3:1:0" # hpf' 5e3 0.2
                  d2 . i . sl 8 -- zp 2
                     . juxBy 0.25 (rev) . iter 4 . str 4
                     . ev 4 (chop 2 . (# pan rand)) . ev 2 ((|+| sp "-2"))
                     . (# sp "[1 1.5 1 2]/4") . (# del "0.5:0.1:0.5")
                     . (# hpf' "[1e3 0.5e3 1e3]/2" 0.1) . (# lpf' "[5e3 2e3 3e3]/3" 0.1)
                     $ sound "cutzpbb3:4(7,16) cutzpbb3:5(3,8)" # gco "1.1:2:1"
                  d3 . i . sl 2 -- pc
                     . ev 8 (fa 2)
                     . ev 4 (# hpf' "1e3 4e3 7e3" "0.1")
                     $ stack [
                         s "bdk2:21(3,8) bdk2:21(3,8)" # go "1:3"
                         ,struct "t(3,8)!2" $ up (sl 4 $ "[0 <-7 [5 5 4]>]!2 [0 -8] [-7 [-10 ~]]" + 1)
                         # s "bssub" # gco "1:5:4" # shape 0.3
                         ,ev 4 ((# sp "-1"). jux (rev)) . fa "1 2"
                         . loopAt 2 . struct "t(3,8)" $ s "jbreaks:100" # gco "1.1:7:5" # shape 0.3
                         # rvb "0.2:0.2"
                         ,sl 4 . (# hpf "2e3:0.1").(# rvb "0.9:0.8").(# del "0.2:0.3:0.6").(# pan rand)
                         $ n (r 4) # s "fxrise" # gco "0.9:3:2"
                       ]


                  hush
                  """,
            embed="""<iframe width="560" height="315" src="https://www.youtube.com/embed/Db0QJo1eaoI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""
            )

    Work(
        createdBy=Hiro,
        created="2018/07/02",
        name="Python abstraction",
        iframe="",
        embed="",
        picture="https://66.media.tumblr.com/0a30785b2846aea9bf3d535d80319a0c/tumblr_ps9jpbjEkG1w3debko1_1280.png",
        github="github link",
        code="""from PIL import Image, ImageDraw, ImageFilter


#im = Image.open("6MzjjikJ_400x400.jpg")
im = Image.open("29.png")

im1 = im.filter(ImageFilter.CONTOUR)
im1 = im.filter(ImageFilter.CONTOUR)
im6 = im1.filter(ImageFilter.BLUR)
im5 = im6.filter(ImageFilter.CONTOUR)
im7 = im5.filter(ImageFilter.CONTOUR)
im8 = im7.filter(ImageFilter.CONTOUR)
im2 = im.filter(ImageFilter.MinFilter(3))
im3 = im.filter(ImageFilter.MinFilter)  # same as MinFilter(3)
im8.save('29.png')
""",
        description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec purus libero, iaculis sit amet nunc a, varius interdum turpis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam ornare ultrices libero, vitae malesuada erat interdum sit amet. Quisque vel felis dignissim, efficitur felis auctor, consequat magna. Phasellus tortor elit, dignissim ac euismod id, fermentum ut turpis. Nullam ex orci, elementum ac felis quis, interdum consequat eros. Etiam pharetra diam ut tincidunt consectetur. Nunc sit amet bibendum diam, et laoreet sapien. Nam aliquam convallis libero ac maximus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed vitae finibus arcu.\n
        \n
        Vivamus cursus placerat ipsum eget suscipit. Sed malesuada diam nec fermentum rutrum. Pellentesque sagittis hendrerit ligula vel placerat. Suspendisse blandit libero sed sapien lacinia, nec finibus leo feugiat. Duis porta sit amet magna nec interdum. Praesent vitae convallis arcu, vitae interdum erat. Vivamus nisi nulla, tincidunt eu ultricies sit amet, placerat et lectus. Integer at erat volutpat, ultricies sapien luctus, pulvinar mauris. Cras eget luctus elit.""",
        medium=illustration
    )

    Work(
        createdBy=Hiro,
        created="2018/07/02",
        name="Javascript Fractals",
        iframe="link.co.uk",
        embed="link.png",
        picture="https://66.media.tumblr.com/2a864fe1e626ae39b0efe245de61acd5/tumblr_psb6544WUj1w3debko1_1280.png",
        github="github link",
        code="heres some code",
        description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec purus libero, iaculis sit amet nunc a, varius interdum turpis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam ornare ultrices libero, vitae malesuada erat interdum sit amet. Quisque vel felis dignissim, efficitur felis auctor, consequat magna. Phasellus tortor elit, dignissim ac euismod id, fermentum ut turpis. Nullam ex orci, elementum ac felis quis, interdum consequat eros. Etiam pharetra diam ut tincidunt consectetur. Nunc sit amet bibendum diam, et laoreet sapien. Nam aliquam convallis libero ac maximus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed vitae finibus arcu.\n
        \n
        Vivamus cursus placerat ipsum eget suscipit. Sed malesuada diam nec fermentum rutrum. Pellentesque sagittis hendrerit ligula vel placerat. Suspendisse blandit libero sed sapien lacinia, nec finibus leo feugiat. Duis porta sit amet magna nec interdum. Praesent vitae convallis arcu, vitae interdum erat. Vivamus nisi nulla, tincidunt eu ultricies sit amet, placerat et lectus. Integer at erat volutpat, ultricies sapien luctus, pulvinar mauris. Cras eget luctus elit.""",
        medium=illustration
    )


    Work(
        createdBy=Molly,
        created="2018/07/02",
        name="SuperMarioClouds.JS",
        iframe="",
        embed="""<iframe width="560" height="315" src="https://www.youtube.com/embed/Pz29DtB6fX4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>""",
        picture="https://66.media.tumblr.com/fff4ebd18455390b89ed52b8af925ecb/tumblr_psbnxw0bfo1w3debko1_1280.png",
        github="",
        code="""import TileResolver from '../TileResolver.js'

export function createBackgroundLayer(level, tiles, sprites) {
    const resolver = new TileResolver(tiles);

    const buffer = document.createElement('canvas');
    buffer.width = 256 + 16;
    buffer.height = 240;

    const context = buffer.getContext('2d');

    function redraw(startIndex, endIndex)  {
        context.clearRect(0, 0, buffer.width, buffer.height);

        for (let x = startIndex; x <= endIndex; ++x) {
            const col = tiles.grid[x];
            if (col) {
                col.forEach((tile, y) => {
                    if (sprites.animations.has(tile.name)) {
                        sprites.drawAnim(tile.name, context, x - startIndex, y, level.totalTime);
                    } else {
                        sprites.drawTile(tile.name, context, x - startIndex, y);
                    }
                });
            }
        }
    }

    return function drawBackgroundLayer(context, camera) {
        const drawWidth = resolver.toIndex(camera.size.x);
        const drawFrom = resolver.toIndex(camera.pos.x);
        const drawTo = drawFrom + drawWidth;
        redraw(drawFrom, drawTo);

        context.drawImage(buffer,
            -camera.pos.x % 16,
            -camera.pos.y);
    };
}""",
        description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec purus libero, iaculis sit amet nunc a, varius interdum turpis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam ornare ultrices libero, vitae malesuada erat interdum sit amet. Quisque vel felis dignissim, efficitur felis auctor, consequat magna. Phasellus tortor elit, dignissim ac euismod id, fermentum ut turpis. Nullam ex orci, elementum ac felis quis, interdum consequat eros. Etiam pharetra diam ut tincidunt consectetur. Nunc sit amet bibendum diam, et laoreet sapien. Nam aliquam convallis libero ac maximus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed vitae finibus arcu.\n
        \n
        Vivamus cursus placerat ipsum eget suscipit. Sed malesuada diam nec fermentum rutrum. Pellentesque sagittis hendrerit ligula vel placerat. Suspendisse blandit libero sed sapien lacinia, nec finibus leo feugiat. Duis porta sit amet magna nec interdum. Praesent vitae convallis arcu, vitae interdum erat. Vivamus nisi nulla, tincidunt eu ultricies sit amet, placerat et lectus. Integer at erat volutpat, ultricies sapien luctus, pulvinar mauris. Cras eget luctus elit.""",
        medium=animation
    )




    Work(
        createdBy=Johnny,
        created="2018/07/02",
        name="Generative Comic",
        iframe="https://tomjhinton.dev/comic.html",
        embed='',
        picture="https://66.media.tumblr.com/0a841d757b11a1c9335f2aa0c821a922/tumblr_psikqz0oyL1w3debko1_1280.png",
        github="",
        code="""
    var c = document.getElementById('myCanvas')
    var ctx = c.getContext('2d')

    var c2 = document.getElementById('myCanvas2')
    var ctx2 = c2.getContext('2d')


    var c3 = document.getElementById('myCanvas3')
    var ctx3 = c3.getContext('2d')


    var button = document.getElementById('redraw')

    function draw(startX, startY, len, angle) {
      const blah = Math.floor(Math.random() * 360)

      ctx.beginPath()
      ctx.save()

      ctx.translate(startX, startY)
      ctx.rotate(angle * Math.PI/blah)
      ctx.moveTo(Math.floor(Math.random() * 9), Math.floor(Math.random() * 9))
      ctx.lineTo(0, -len)
      ctx.stroke()
      ctx.strokeStyle = 'rgba(0,0,0,0.8)'
      ctx.lineWidth = Math.random()


      if(len < 8) {
        ctx.restore()
        return
      }

      draw(0, -len, len*0.72, Math.random() * 50)
      draw(0, -len, len*0.72, Math.random() * 50)

      ctx.restore()
    }


    function draw2(startX, startY, len, angle) {
      const blah = Math.floor(Math.random() * 360)
      ctx2.beginPath()
      ctx2.save()

      ctx2.translate(startX, startY)
      ctx2.rotate(angle * Math.PI/blah)
      ctx2.moveTo(Math.floor(Math.random() * 9), Math.floor(Math.random() * 9))
      ctx2.lineTo(0, -len)
      ctx2.stroke()
      ctx2.strokeStyle = 'rgba(0,0,0,0.8)'
      ctx2.lineWidth = Math.random()


      if(len < 10) {
        ctx.restore()
        return
      }

      draw2(0, -len, len*0.9, Math.random() * 50)
      draw2(0, -len, len*0.8, Math.random() * 50)

      ctx2.restore()
    }

    function draw3(startX, startY, len, angle) {
      const blah = Math.floor(Math.random() * 360)

      ctx3.beginPath()
      ctx3.save()

      ctx3.translate(startX, startY)
      ctx3.rotate(angle * Math.PI/blah)
      ctx3.moveTo(Math.floor(Math.random() * 9), Math.floor(Math.random() * 9))
      ctx3.lineTo(-3, -len)
      ctx3.lineStyle = 'rgba(0,0,0,0.8)'
      ctx3.stroke()
      ctx3.strokeStyle = 'rgba(0,0,0,0.8)'
      ctx3.lineWidth = Math.random()



      if(len < 8) {
        ctx.restore()
        return
      }

      draw3(0, -len, len*0.8, Math.random() * 50)
      draw3(0, -len, len*0.8, Math.random() * 50)

      ctx3.restore()
    }

    button.addEventListener('click', function () {

      drawComics()


    })


    function drawComics(){

      //draw(450, 700, 250, -10)
      draw(Math.floor(Math.random() * 500), Math.floor(Math.random() * 500), 20  + Math.floor(Math.random() * 180), -10)
      draw(Math.floor(Math.random() * 500), Math.floor(Math.random() * 500), 20 + Math.floor(Math.random() * 200), 5)
      //draw3(150, 200, 250, 10)
      draw2(Math.floor(Math.random() * 500), Math.floor(Math.random() * 500), 20 + Math.floor(Math.random() * 200), 1)
      draw2(Math.floor(Math.random() * 500), Math.floor(Math.random() * 500), 50 + Math.floor(Math.random() * 200), 1)
      //draw(900, 200, 250, 10)
      draw3(Math.floor(Math.random() * 500),20 + Math.floor(Math.random() * 500), Math.floor(Math.random() * 200), 20)
      draw3(Math.floor(Math.random() * 500), 20 + Math.floor(Math.random() * 500), Math.floor(Math.random() * 200), 20)

    }

    drawComics()
""",
        description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec purus libero, iaculis sit amet nunc a, varius interdum turpis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam ornare ultrices libero, vitae malesuada erat interdum sit amet. Quisque vel felis dignissim, efficitur felis auctor, consequat magna. Phasellus tortor elit, dignissim ac euismod id, fermentum ut turpis. Nullam ex orci, elementum ac felis quis, interdum consequat eros. Etiam pharetra diam ut tincidunt consectetur. Nunc sit amet bibendum diam, et laoreet sapien. Nam aliquam convallis libero ac maximus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed vitae finibus arcu.\n
        \n
        Vivamus cursus placerat ipsum eget suscipit. Sed malesuada diam nec fermentum rutrum. Pellentesque sagittis hendrerit ligula vel placerat. Suspendisse blandit libero sed sapien lacinia, nec finibus leo feugiat. Duis porta sit amet magna nec interdum. Praesent vitae convallis arcu, vitae interdum erat. Vivamus nisi nulla, tincidunt eu ultricies sit amet, placerat et lectus. Integer at erat volutpat, ultricies sapien luctus, pulvinar mauris. Cras eget luctus elit.""",
        medium=application
    )










    Ad(
        name="Looking for an Illustartor",
        createdBy=company,
        created="2018/07/02",
        description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec purus libero, iaculis sit amet nunc a, varius interdum turpis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam ornare ultrices libero, vitae malesuada erat interdum sit amet. Quisque vel felis dignissim, efficitur felis auctor, consequat magna. Phasellus tortor elit, dignissim ac euismod id, fermentum ut turpis. Nullam ex orci, elementum ac felis quis, interdum consequat eros. Etiam pharetra diam ut tincidunt consectetur. Nunc sit amet bibendum diam, et laoreet sapien. Nam aliquam convallis libero ac maximus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed vitae finibus arcu.\n
        \n
        Vivamus cursus placerat ipsum eget suscipit. Sed malesuada diam nec fermentum rutrum. Pellentesque sagittis hendrerit ligula vel placerat. Suspendisse blandit libero sed sapien lacinia, nec finibus leo feugiat. Duis porta sit amet magna nec interdum. Praesent vitae convallis arcu, vitae interdum erat. Vivamus nisi nulla, tincidunt eu ultricies sit amet, placerat et lectus. Integer at erat volutpat, ultricies sapien luctus, pulvinar mauris. Cras eget luctus elit.""",
        medium=illustration
    )


    Ad(
    name="Need music for a project",
    createdBy=cyberdyne,
    created="2018/07/02",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec purus libero, iaculis sit amet nunc a, varius interdum turpis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam ornare ultrices libero, vitae malesuada erat interdum sit amet. Quisque vel felis dignissim, efficitur felis auctor, consequat magna. Phasellus tortor elit, dignissim ac euismod id, fermentum ut turpis. Nullam ex orci, elementum ac felis quis, interdum consequat eros. Etiam pharetra diam ut tincidunt consectetur. Nunc sit amet bibendum diam, et laoreet sapien. Nam aliquam convallis libero ac maximus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed vitae finibus arcu.\n
    \n
    Vivamus cursus placerat ipsum eget suscipit. Sed malesuada diam nec fermentum rutrum. Pellentesque sagittis hendrerit ligula vel placerat. Suspendisse blandit libero sed sapien lacinia, nec finibus leo feugiat. Duis porta sit amet magna nec interdum. Praesent vitae convallis arcu, vitae interdum erat. Vivamus nisi nulla, tincidunt eu ultricies sit amet, placerat et lectus. Integer at erat volutpat, ultricies sapien luctus, pulvinar mauris. Cras eget luctus elit.""",
    medium=music
    )



    db.commit()
