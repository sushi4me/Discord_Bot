import asyncio
import asyncpg
import discord
import json

from discord.ext import commands


class PostgreSQL:
    def __init__(self, server_bot):
        self.server_bot = server_bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def explain(self, ctx, column: str, table: str):
        """*explain <column> <table>
        A command that will explain and analyze a column/table in the database.
        """

        embed = discord.Embed(colour=discord.Colour.purple())

        async with self.server_bot.pool.acquire() as connection:
            statement = await connection.prepare(f"SELECT {column} FROM {table}")
            explain = await statement.explain(analyze=True)
            explain = json.dumps(explain, indent=4)

            embed.add_field(name=f"'SELECT {column} FROM {table}'", value=explain)

        await ctx.send(embed=embed)

    @commands.command()
    async def register(self, ctx):
        """*register
        A command that will register the author of the message in the database.
        """

        discord_id = str(ctx.message.author.id)

        async with self.server_bot.pool.acquire() as connection:
            try:
                async with connection.transaction():
                    await connection.execute('INSERT INTO users (discord_id) VALUES ($1)', (discord_id))
                    await ctx.send('You are now registered in the database.')
            except asyncpg.exceptions.UniqueViolationError:
                await ctx.send('You are already a registered member in the database.')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def store(self, ctx):
        """*store
        A command that inserts every available command into the database.
        """

        for commands in self.server_bot.commands:
            commands = commands.name

            async with self.server_bot.pool.acquire() as connection:
                async with connection.transaction():
                    await connection.execute('INSERT INTO commands (command) VALUES ($1)', (commands))

        await ctx.send('All commands have been stored in the database.')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def truncate(self, ctx, table: str):
        """*truncate <table>
        A command that will truncate a table in the database.
        """

        async with self.server_bot.pool.acquire() as connection:
            try:
                async with connection.transaction():
                    await connection.execute(f"TRUNCATE {table} RESTART IDENTITY;")
                await ctx.send(f"The table `{table}` was truncated.")
            except asyncpg.exceptions.UndefinedTableError:
                await ctx.send(f"**Error:**: `{table}` does not exist.")


def setup(sever_bot):
    server_bot.add_cog(PostgreSQL(server_bot))